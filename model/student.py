from db_config import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS STUDENT (
        StudentID INT PRIMARY KEY,
        Name VARCHAR(100) NOT NULL,
        Email VARCHAR(100) NOT NULL,
        Department VARCHAR(100) NOT NULL,
        Semester VARCHAR(50) NOT NULL
    )
''')
conn.commit()

def insert_student(sid, name, email, dept, sem):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO STUDENT (StudentID, Name, Email, Department, Semester) VALUES (%s, %s, %s, %s, %s)",
            (sid, name, email, dept, sem)
        )
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def fetch_students():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM STUDENT")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def fetch_student_by_id(sid):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM STUDENT WHERE StudentID = %s", (sid,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def update_student(sid, name, email, dept, sem):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE STUDENT SET Name = %s, Email = %s, Department = %s, Semester = %s WHERE StudentID = %s",
            (name, email, dept, sem, sid)
        )
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def delete_student(sid):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM STUDENT WHERE StudentID = %s", (sid,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
