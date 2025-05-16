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
cursor.close()
conn.close()