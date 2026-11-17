"""
CONTROLLER - students and departments
Owner: Task 6
Deadline: Sat 14

Endpoints:
    GET /api/departments   list departments for the dropdown (no login needed)
    GET /api/me            the logged-in student's profile
    GET /api/students      list all students (ADMIN ONLY)

Notes:
- Logged in means "student_id" in session      -> otherwise 401
- Admin means session["role"] == "admin"       -> otherwise 403
- Dates from MySQL come back as date objects; convert with str() before jsonify
- Always reply with JSON: {"status": "success", "data": ...}
"""

from datetime import date, datetime
from flask import Blueprint, jsonify, session
from models import student_model

student_bp = Blueprint("students", __name__, url_prefix="/api")

def convert_dates(obj):
    if isinstance(obj, list):
        return [convert_dates(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: str(v) if isinstance(v, (date, datetime)) else v for k, v in obj.items()}
    elif isinstance(obj, (date, datetime)):
        return str(obj)
    return obj

@student_bp.route("/departments", methods=["GET"])
def list_departments(): 
    # no login needed for departments dropdown
    try:
        departments = student_model.get_departments()
        return jsonify({
            "status": "success",
            "data": convert_dates(departments)
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@student_bp.route("/me", methods=["GET"])
def my_profile():
    # get logged in students profile
    if "student_id" not in session:
        return jsonify({"status": "error", "message": "Not logged in"}), 401
    try:
        student_id = session["student_id"]
        profile = student_model.get_student_profile(student_id)
       
        if not profile:
            return jsonify({"status": "error", "message": "Student profile not found"}), 404
       
        return jsonify({
            "status": "success",
            "data": convert_dates(profile)
        }), 200 
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@student_bp.route("/students", methods=["GET"])
def list_students():
    # list all students, admin only

    if session.get("role") != "admin":
        return jsonify({"status": "error", "message": "Forbidden: Admin access required"}), 403
    
    try:
        students = student_model.get_all_students()
        return jsonify({
            "status": "success",
            "data": convert_dates(students)
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500