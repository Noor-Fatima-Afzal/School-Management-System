from db_config import get_connection

# Create MARKS table (executed only once)
conn = get_connection()
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS MARKS (
        MarkID INT PRIMARY KEY AUTO_INCREMENT,
        StudentID INT,
        CourseID INT,
        MarksObtained FLOAT,
        FOREIGN KEY (StudentID) REFERENCES STUDENT(StudentID),
        FOREIGN KEY (CourseID) REFERENCES COURSE(CourseID)
    )
''')
conn.commit()
cursor.close()
conn.close()

# Function to add marks
def add_marks(student_id, course_id, marks_obtained):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO MARKS (StudentID, CourseID, MarksObtained) VALUES (%s, %s, %s)",
            (student_id, course_id, marks_obtained)
        )
        conn.commit()
        print("Marks added successfully.")
    except Exception as e:
        print("Error adding marks:", e)
    finally:
        cursor.close()
        conn.close()

# Function to fetch all marks
def fetch_marks():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM MARKS")
        return cursor.fetchall()
    except Exception as e:
        print("Error fetching marks:", e)
        return []
    finally:
        cursor.close()
        conn.close()

# Function to update marks by MarkID
def update_marks(mark_id, student_id=None, course_id=None, marks_obtained=None):
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
        if marks_obtained is not None:
            updates.append("MarksObtained = %s")
            values.append(marks_obtained)

        if updates:
            query = "UPDATE MARKS SET " + ", ".join(updates) + " WHERE MarkID = %s"
            values.append(mark_id)
            cursor.execute(query, tuple(values))
            conn.commit()
            print("Marks updated successfully.")
        else:
            print("No fields to update.")
    except Exception as e:
        print("Error updating marks:", e)
    finally:
        cursor.close()
        conn.close()

# Function to delete marks by MarkID
def delete_marks(mark_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM MARKS WHERE MarkID = %s", (mark_id,))
        conn.commit()
        print("Marks deleted successfully.")
    except Exception as e:
        print("Error deleting marks:", e)
    finally:
        cursor.close()
        conn.close()
