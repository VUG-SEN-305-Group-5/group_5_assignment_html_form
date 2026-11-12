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
  conn = get_connection()
  # Use dictionary=True if using mysql-connector, or let PyMySQL cursorclass handle it.
  # Let's write it safely:
  cursor = conn.cursor()
  try:
    cursor.execute(
        "SELECT department_id, department_name, faculty FROM departments;"
    )
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
  finally:
    cursor.close()
    conn.close()


def create_student(data, conn):
  cursor = conn.cursor()
  try:
    query = """
            INSERT INTO students 
            (matric_no, first_name, last_name, other_name, email, phone, date_of_birth, gender, department_id, level, state_of_origin, address)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    params = (
        data.get("matric_no"),
        data.get("first_name"),
        data.get("last_name"),
        data.get("other_name"),
        data.get("email"),
        data.get("phone"),
        data.get("date_of_birth"),
        data.get("gender"),
        data.get("department_id"),
        data.get("level"),
        data.get("state_of_origin"),
        data.get("address"),
    )
    cursor.execute(query, params)
    return cursor.lastrowid
  finally:
    cursor.close()


def get_student_by_id(student_id):
  conn = get_connection()
  cursor = conn.cursor()
  try:
    query = """
            SELECT s.*, d.department_name, d.faculty
            FROM students s
            JOIN departments d ON s.department_id = d.department_id
            WHERE s.student_id = %s
        """
    cursor.execute(query, (student_id,))
    row = cursor.fetchone()
    if not row:
      return None
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
  finally:
    cursor.close()
    conn.close()


def get_all_students():
  conn = get_connection()
  cursor = conn.cursor()
  try:
    query = """
            SELECT s.*, d.department_name, d.faculty
            FROM students s
            JOIN departments d ON s.department_id = d.department_id
            ORDER BY s.created_at DESC
        """
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
  finally:
    cursor.close()
    conn.close()


def matric_exists(matric_no):
  conn = get_connection()
  cursor = conn.cursor()
  try:
    query = "SELECT 1 FROM students WHERE matric_no = %s LIMIT 1;"
    cursor.execute(query, (matric_no,))
    return cursor.fetchone() is not None
  finally:
    cursor.close()
    conn.close()


def email_exists(email):
  conn = get_connection()
  cursor = conn.cursor()
  try:
    query = "SELECT 1 FROM students WHERE email = %s LIMIT 1;"
    cursor.execute(query, (email,))
    return cursor.fetchone() is not None
  finally:
    cursor.close()
    conn.close()


def phone_exists(phone):
  conn = get_connection()
  cursor = conn.cursor()
  try:
    query = "SELECT 1 FROM students WHERE phone = %s LIMIT 1;"
    cursor.execute(query, (phone,))
    return cursor.fetchone() is not None
  finally:
    cursor.close()
    conn.close()