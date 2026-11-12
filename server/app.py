from flask import Flask, jsonify
from config import Config
from db import get_connection

from routes.auth_routes import auth_bp
from routes.student_routes import student_bp
from models.student_model import get_all_departments, get_all_students

# serve the frontend from the client folder next to this one
app = Flask(__name__, static_folder="../client", static_url_path="")
app.config.from_object(Config)

# plug in the API routes
app.register_blueprint(auth_bp)
app.register_blueprint(student_bp)


# ---------------- pages ----------------

print("Departments:", get_all_departments())
print("Students:", get_all_students())

@app.route("/")
@app.route("/register")
def register_page():
    return app.send_static_file("register.html")


@app.route("/login")
def login_page():
    return app.send_static_file("login.html")


@app.route("/dashboard")
def dashboard_page():
    return app.send_static_file("dashboard.html")


# ---------------- health check ----------------

@app.route("/api/health")
def health_check():
    """Confirms Flask can talk to the database."""
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS total FROM departments")
            result = cursor.fetchone()
        conn.close()
        return jsonify({"status": "ok", "departments_found": result["total"]})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=Config.PORT)