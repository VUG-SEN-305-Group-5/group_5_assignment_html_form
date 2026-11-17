"""
CONTROLLER - authentication
Owner: Task 5
Deadline: Sat 14

Endpoints:
    POST /api/register   create a student + their login
    POST /api/login      check username/password, start a session
    POST /api/logout     clear the session
"""

import re

from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

from db import get_connection
from models import student_model, auth_model

auth_bp = Blueprint("auth", __name__, url_prefix="/api")

MATRIC_PATTERN = re.compile(r"^[A-Z]{3}/[A-Z]{3}/\d{2}/\d{4,6}$")
EMAIL_PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
PHONE_PATTERN = re.compile(r"^0\d{10}$")

REQUIRED_FIELDS = [
    "first_name", "last_name", "matric_no", "email", "phone", "date_of_birth",
    "gender", "department_id", "level", "state_of_origin", "username",
    "password", "confirm_password",
]


def error(message, code):
    return jsonify({"status": "error", "message": message}), code


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True) or {}

    # clean up text fields
    for key, value in data.items():
        if isinstance(value, str) and key not in ("password", "confirm_password"):
            data[key] = value.strip()
    data["matric_no"] = str(data.get("matric_no", "")).upper()

    # 1. validate again - never trust the browser
    missing = [f for f in REQUIRED_FIELDS if not data.get(f)]
    if missing:
        return error(f"Missing required fields: {', '.join(missing)}", 400)
    if not MATRIC_PATTERN.match(data["matric_no"]):
        return error("Matric number must look like VUG/SEN/24/11362", 400)
    if not EMAIL_PATTERN.match(data["email"]):
        return error("Enter a valid email address", 400)
    if not PHONE_PATTERN.match(str(data["phone"])):
        return error("Phone number must be 11 digits starting with 0", 400)
    if data["gender"] not in ("Male", "Female"):
        return error("Gender must be Male or Female", 400)
    if int(data["level"]) not in (100, 200, 300, 400, 500):
        return error("Level must be 100 to 500", 400)
    if len(data["username"]) < 3:
        return error("Username must have at least 3 characters", 400)
    if len(data["password"]) < 8:
        return error("Password must be at least 8 characters", 400)
    if data["password"] != data["confirm_password"]:
        return error("Passwords do not match", 400)

    # 2. check for duplicates
    if student_model.matric_exists(data["matric_no"]):
        return error("This matric number is already registered", 409)
    if student_model.email_exists(data["email"]):
        return error("This email is already registered", 409)
    if student_model.phone_exists(data["phone"]):
        return error("This phone number is already registered", 409)
    if auth_model.username_exists(data["username"]):
        return error("This username is taken", 409)

    # 3. save student + login together (both or nothing)
    conn = get_connection()
    try:
        student_id = student_model.create_student(data, conn)
        password_hash = generate_password_hash(data["password"])
        auth_model.create_credentials(student_id, data["username"], password_hash, conn)
        conn.commit()
    except Exception as e:
        conn.rollback()
        return error(f"Registration failed: {e}", 500)
    finally:
        conn.close()

    return jsonify({
        "status": "success",
        "message": "Account created successfully. You can now log in.",
        "data": {"student_id": student_id, "username": data["username"]},
    }), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = str(data.get("username", "")).strip()
    password = data.get("password", "")

    if not username or not password:
        return error("Username and password are required", 400)

    user = auth_model.get_user_by_username(username)

    # same message for wrong username and wrong password
    if not user or not check_password_hash(user["password_hash"], password):
        return error("Invalid username or password", 401)
    if not user["is_active"]:
        return error("This account has been deactivated", 403)

    auth_model.update_last_login(user["credential_id"])

    session.clear()
    session["student_id"] = user["student_id"]
    session["username"] = user["username"]
    session["role"] = user["role"]

    return jsonify({
        "status": "success",
        "message": "Login successful",
        "data": {"username": user["username"], "role": user["role"]},
    }), 200


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"status": "success", "message": "Logged out"}), 200