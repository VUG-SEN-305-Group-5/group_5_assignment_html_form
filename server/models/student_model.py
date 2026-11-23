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

Note: db.py uses DictCursor, so every row already comes back as a dict.
"""

from db import get_connection


def get_all_departments():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT department_id, department_name, faculty "
                "FROM departments ORDER BY department_name"
            )
            return cursor.fetchall()
    finally:
        conn.close()


def create_student(data, conn):
    """Uses the connection passed in. Does NOT commit - auth_routes commits
    once after the student and their login are both inserted."""
    with conn.cursor() as cursor:
        query = """
            INSERT INTO students
            (matric_no, first_name, last_name, other_name, email, phone,
             date_of_birth, gender, department_id, level, state_of_origin, address)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            data.get("matric_no"),
            data.get("first_name"),
            data.get("last_name"),
            data.get("other_name") or None,
            data.get("email"),
            data.get("phone"),
            data.get("date_of_birth"),
            data.get("gender"),
            data.get("department_id"),
            data.get("level"),
            data.get("state_of_origin"),
            data.get("address") or None,
        )
        cursor.execute(query, params)
        return cursor.lastrowid


def get_student_by_id(student_id):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            query = """
                SELECT s.*, d.department_name, d.faculty
                FROM students s
                JOIN departments d ON s.department_id = d.department_id
                WHERE s.student_id = %s
            """
            cursor.execute(query, (student_id,))
            return cursor.fetchone()
    finally:
        conn.close()


def get_all_students():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            query = """
                SELECT s.*, d.department_name, d.faculty
                FROM students s
                JOIN departments d ON s.department_id = d.department_id
                ORDER BY s.created_at DESC
            """
            cursor.execute(query)
            return cursor.fetchall()
    finally:
        conn.close()


def _exists(column, value):
    """Shared helper for the *_exists checks below."""
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT 1 FROM students WHERE {column} = %s LIMIT 1", (value,))
            return cursor.fetchone() is not None
    finally:
        conn.close()


def matric_exists(matric_no):
    return _exists("matric_no", matric_no)


def email_exists(email):
    return _exists("email", email)


def phone_exists(phone):
    return _exists("phone", phone)