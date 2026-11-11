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

from flask import Blueprint, jsonify, session

from models import student_model

student_bp = Blueprint("students", __name__, url_prefix="/api")


@student_bp.route("/departments", methods=["GET"])
def list_departments():
    # TODO
    return jsonify({"status": "error", "message": "Not implemented yet"}), 501


@student_bp.route("/me", methods=["GET"])
def my_profile():
    # TODO
    return jsonify({"status": "error", "message": "Not implemented yet"}), 501


@student_bp.route("/students", methods=["GET"])
def list_students():
    # TODO
    return jsonify({"status": "error", "message": "Not implemented yet"}), 501