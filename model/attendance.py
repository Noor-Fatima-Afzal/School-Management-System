from db_config import get_connection

# Create ATTENDANCE table (executed only once)
conn = get_connection()
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ATTENDANCE (
        AttendanceID INT PRIMARY KEY AUTO_INCREMENT,
        StudentID INT,
        CourseID INT,
        Date DATE,
        Status ENUM('Present', 'Absent') NOT NULL,
        FOREIGN KEY (StudentID) REFERENCES STUDENT(StudentID),
        FOREIGN KEY (CourseID) REFERENCES COURSE(CourseID)
    )
''')
conn.commit()
cursor.close()
conn.close()

# Function to add an attendance record
def add_attendance(student_id, course_id, date, status):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO ATTENDANCE (StudentID, CourseID, Date, Status) VALUES (%s, %s, %s, %s)",
            (student_id, course_id, date, status)
        )
        conn.commit()
        print("Attendance record added successfully.")
    except Exception as e:
        print("Error adding attendance record:", e)
    finally:
        cursor.close()
        conn.close()

# Function to fetch all attendance records
def fetch_attendance():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM ATTENDANCE")
        return cursor.fetchall()
    except Exception as e:
        print("Error fetching attendance records:", e)
        return []
    finally:
        cursor.close()
        conn.close()

# Function to update an attendance record
def update_attendance(attendance_id, student_id=None, course_id=None, date=None, status=None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        updates = []
        values = []

        if student_id is not None:
            updates.append("StudentID = %s")
            values.append(student_id)
        if course_id is not None:
            updates.append("CourseID = %s")
            values.append(course_id)
        if date is not None:
            updates.append("Date = %s")
            values.append(date)
        if status is not None:
            updates.append("Status = %s")
            values.append(status)

        if updates:
            query = "UPDATE ATTENDANCE SET " + ", ".join(updates) + " WHERE AttendanceID = %s"
            values.append(attendance_id)
            cursor.execute(query, tuple(values))
            conn.commit()
            print("Attendance record updated successfully.")
        else:
            print("No fields to update.")
    except Exception as e:
        print("Error updating attendance record:", e)
    finally:
        cursor.close()
        conn.close()

# Function to delete an attendance record
def delete_attendance(attendance_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM ATTENDANCE WHERE AttendanceID = %s", (attendance_id,))
        conn.commit()
        print("Attendance record deleted successfully.")
    except Exception as e:
        print("Error deleting attendance record:", e)
    finally:
        cursor.close()
        conn.close()
