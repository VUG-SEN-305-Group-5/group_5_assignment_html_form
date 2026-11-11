import pymysql
from config import Config


def get_connection():
    """Opens a new connection to the MySQL database.

    Rows come back as dictionaries, e.g. {"matric_no": "...", "email": "..."}
    instead of tuples, so we can use row["email"] instead of row[3].

    Whoever calls this must close the connection when done.
    """
    return pymysql.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False
    )