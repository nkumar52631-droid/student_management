
import sqlite3

def get_connection():
    conn = sqlite3.connect("students.db", timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_connection()

    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                register_number TEXT UNIQUE NOT NULL,
                email TEXT,
                department TEXT
            )
        """)
        conn.commit()

    finally:
        conn.close()
