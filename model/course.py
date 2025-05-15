from db_config import get_connection

# Create table if not exists
conn = get_connection()
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS COURSE (
        CourseID INT PRIMARY KEY,
        CourseName VARCHAR(100) NOT NULL,
        Credits INT NOT NULL,
        Department VARCHAR(100) NOT NULL
    )
''')
conn.commit()

# Function to add a course
def add_course(course_id, course_name, credits, department):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO COURSE (CourseID, CourseName, Credits, Department) VALUES (%s, %s, %s, %s)",
            (course_id, course_name, credits, department)
        )
        conn.commit()
        print("Course added successfully.")
    except Exception as e:
        print("Error adding course:", e)
    finally:
        cursor.close()
        conn.close()

# Function to fetch all courses
def fetch_courses():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM COURSE")
        courses = cursor.fetchall()
        return courses
    except Exception as e:
        print("Error fetching courses:", e)
        return []
    finally:
        cursor.close()
        conn.close()

# Function to update a course
def update_course(course_id, course_name=None, credits=None, department=None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        updates = []
        values = []

        if course_name:
            updates.append("CourseName = %s")
            values.append(course_name)
        if credits:
            updates.append("Credits = %s")
            values.append(credits)
        if department:
            updates.append("Department = %s")
            values.append(department)

        if updates:
            update_query = "UPDATE COURSE SET " + ", ".join(updates) + " WHERE CourseID = %s"
            values.append(course_id)
            cursor.execute(update_query, tuple(values))
            conn.commit()
            print("Course updated successfully.")
        else:
            print("No fields to update.")
    except Exception as e:
        print("Error updating course:", e)
    finally:
        cursor.close()
        conn.close()

# Function to delete a course
def delete_course(course_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM COURSE WHERE CourseID = %s", (course_id,))
        conn.commit()
        print("Course deleted successfully.")
    except Exception as e:
        print("Error deleting course:", e)
    finally:
        cursor.close()
        conn.close()
