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
cursor.close()
conn.close()