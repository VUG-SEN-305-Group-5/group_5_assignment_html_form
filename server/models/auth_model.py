"""
MODEL - user_credentials (login details)
Owner: Task 4
Deadline: Fri 13

Rules for this file:
- Only SQL lives here. No Flask, no request, no jsonify.
- This file NEVER sees the plain password, only password_hash.
  Hashing happens in routes/auth_routes.py.
- Always use %s placeholders.
- Functions that open their own connection must call conn.commit()
  when they change data.
- create_credentials() is the exception: it uses the connection passed in
  and does NOT commit, because auth_routes.py saves the student and their
  login together and commits once (both or nothing).
"""

from db import get_connection


def create_credentials(student_id, username, password_hash, conn, role="student"):
    """Inserts a login for a student. Returns the new credential_id.

    Uses the caller's connection and does NOT commit - the caller commits
    after the student row and this row are both inserted.
    """
    with conn.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO user_credentials (student_id, username, password_hash, role)
            VALUES (%s, %s, %s, %s)
            """,
            (student_id, username, password_hash, role),
        )
        return cursor.lastrowid


def get_user_by_username(username):
    """Returns the login row for this username as a dict, or None.

    Includes password_hash so the route can check the password.
    Never send this row straight back to the browser.
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT credential_id, student_id, username, password_hash, role, is_active
                FROM user_credentials
                WHERE username = %s
                """,
                (username,),
            )
            return cursor.fetchone()
    finally:
        conn.close()


def username_exists(username):
    """Returns True if the username is already taken."""
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT 1 FROM user_credentials WHERE username = %s LIMIT 1", (username,)
            )
            return cursor.fetchone() is not None
    finally:
        conn.close()


def update_last_login(credential_id):
    """Sets last_login to the current time after a successful login."""
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE user_credentials SET last_login = NOW() WHERE credential_id = %s",
                (credential_id,),
            )
        conn.commit()
    finally:
        conn.close()
