"""
MODEL - students and departments
Owner: Task 3
Deadline: Fri 13

Rules for this file:
- Only SQL lives here. No Flask, no request, no jsonify.
- Always use %s placeholders, never put values into the SQL string yourself
  (this stops SQL injection).
- Open a connection with get_connection() and close it when done.
- Functions that change data (INSERT/UPDATE/DELETE) must call conn.commit().
"""

from db import get_connection


def get_all_departments():
    """Return every department as a list of dicts.
    e.g. [{"department_id": 1, "department_name": "Software Engineering", "faculty": "Computing"}, ...]
    """
    # TODO
    pass


def create_student(data, conn):
    """Insert a new student and return the new student_id.

    data is a dict with: matric_no, first_name, last_name, other_name, email,
    phone, date_of_birth, gender, department_id, level, state_of_origin, address

    Use the conn that is passed in and DON'T commit or close it.
    auth_routes saves the student and their login on the same connection,
    then commits once, so both are saved together or neither is.
    Hint: cursor.lastrowid gives the new id.
    """
    # TODO
    pass


def get_student_by_id(student_id):
    """Return one student with their department_name (JOIN departments), or None."""
    # TODO
    pass


def get_all_students():
    """Return all students with their department_name, newest first."""
    # TODO
    pass


def matric_exists(matric_no):
    """Return True if this matric number is already registered."""
    # TODO
    pass


def email_exists(email):
    """Return True if this email is already registered."""
    # TODO
    pass


def phone_exists(phone):
    """Return True if this phone number is already registered."""
    # TODO
    pass