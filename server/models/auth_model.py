"""
MODEL - user_credentials (login details)
Owner: Task 4
Deadline: Fri 13

Rules for this file:
- Only SQL lives here. No Flask, no request, no jsonify.
- This file NEVER sees the plain password, only password_hash.
  Hashing happens in routes/auth_routes.py.
- Always use %s placeholders.
- Functions that change data must call conn.commit().
"""

from db import get_connection


def create_credentials(student_id, username, password_hash, conn, role="student"):
    """Insert a login row for a student and return the new credential_id.

    Use the conn that is passed in and DON'T commit or close it
    (auth_routes commits once after both the student and the login are inserted).
    """
    # TODO
    pass


def get_user_by_username(username):
    """Return the credentials row for this username, or None.
    Must include: credential_id, student_id, username, password_hash, role, is_active
    """
    # TODO
    pass


def username_exists(username):
    """Return True if the username is taken."""
    # TODO
    pass


def update_last_login(credential_id):
    """Set last_login to the current date and time (NOW())."""
    # TODO
    pass