from db_config import get_connection

# Table creation (executed only once)
conn = get_connection()
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS FEE (
        FeeID INT PRIMARY KEY AUTO_INCREMENT,
        StudentID INT,
        Amount DECIMAL(10, 2),
        PaidDate DATE,
        Status ENUM('Paid', 'Unpaid') NOT NULL,
        FOREIGN KEY (StudentID) REFERENCES STUDENT(StudentID)
    )
''')
conn.commit()
cursor.close()
conn.close()
