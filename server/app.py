from flask import Flask, jsonify
from config import Config
from db import get_connection

# serve the frontend from the client folder next to this one
app = Flask(__name__, static_folder="../client", static_url_path="")
app.config.from_object(Config)


@app.route("/")
def home():
    return app.send_static_file("register.html")


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