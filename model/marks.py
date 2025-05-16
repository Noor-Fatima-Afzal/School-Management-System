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
