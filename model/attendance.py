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