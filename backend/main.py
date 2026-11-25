
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import create_table, get_connection

# Create FastAPI application
app = FastAPI()

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database table
create_table()


@app.get("/")
def home():
    return {"message": "Student Management System is Running"}


@app.post("/students")
def add_student(
    name: str,
    register_number: str,
    email: str,
    department: str
):
    conn = get_connection()

    try:
        conn.execute(
            """INSERT INTO students
            (name, register_number, email, department)
            VALUES (?, ?, ?, ?)""",
            (name, register_number, email, department)
        )

        conn.commit()

        return {"message": "Student added successfully"}

    finally:
        conn.close()


@app.get("/students")
def get_students():
    conn = get_connection()

    try:
        students = conn.execute(
            "SELECT * FROM students"
        ).fetchall()

        return [dict(student) for student in students]

    finally:
        conn.close()
