"""
CONTROLLER - authentication
Owner: Task 5
Deadline: Sat 14

Endpoints:
    POST /api/register   create a student + their login
    POST /api/login      check username/password, start a session
    POST /api/logout     clear the session

Notes:
- Read the JSON body with request.get_json()
- Hash passwords with generate_password_hash() and check them with
  check_password_hash() (from werkzeug, already installed with Flask)
- Validate again here even though the frontend validates - never trust the browser
- On login success store session["student_id"], session["username"], session["role"]
- Always reply with JSON:
    success: {"status": "success", "message": "...", "data": {...}}  -> 200 or 201
    failure: {"status": "error", "message": "..."}                   -> 400 / 401 / 409
"""

from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

from db import get_connection
from models import student_model, auth_model

auth_bp = Blueprint("auth", __name__, url_prefix="/api")


@auth_bp.route("/register", methods=["POST"])
def register():
    # TODO
    # 1. get the JSON body
    # 2. check required fields, phone/email/matric format,
    #    password == confirm_password, password at least 8 characters  -> 400
    # 3. check matric/email/phone/username are not already taken        -> 409
    # 4. conn = get_connection()
    #    student_id = student_model.create_student(data, conn)
    #    auth_model.create_credentials(student_id, username, hashed, conn)
    #    conn.commit()
    #    if anything fails: conn.rollback()
    #    finally: conn.close()
    # 5. return 201
    return jsonify({"status": "error", "message": "Not implemented yet"}), 501


@auth_bp.route("/login", methods=["POST"])
def login():
    # TODO
    # 1. get username and password from the JSON body
    # 2. find the user, check is_active, check the password -> 401 if wrong
    #    (same message for wrong username AND wrong password)
    # 3. update_last_login, save details in the session
    # 4. return 200 with the role so the frontend knows where to go
    return jsonify({"status": "error", "message": "Not implemented yet"}), 501


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"status": "success", "message": "Logged out"}), 200