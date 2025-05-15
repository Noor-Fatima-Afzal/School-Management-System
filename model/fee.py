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

# Function to add a fee record
def add_fee(student_id, amount, paid_date, status):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO FEE (StudentID, Amount, PaidDate, Status) VALUES (%s, %s, %s, %s)",
            (student_id, amount, paid_date, status)
        )
        conn.commit()
        print("Fee record added successfully.")
    except Exception as e:
        print("Error adding fee record:", e)
    finally:
        cursor.close()
        conn.close()

# Function to fetch all fee records
def fetch_fees():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM FEE")
        return cursor.fetchall()
    except Exception as e:
        print("Error fetching fee records:", e)
        return []
    finally:
        cursor.close()
        conn.close()

# Function to update a fee record by FeeID
def update_fee(fee_id, student_id=None, amount=None, paid_date=None, status=None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        updates = []
        values = []

        if student_id is not None:
            updates.append("StudentID = %s")
            values.append(student_id)
        if amount is not None:
            updates.append("Amount = %s")
            values.append(amount)
        if paid_date is not None:
            updates.append("PaidDate = %s")
            values.append(paid_date)
        if status is not None:
            updates.append("Status = %s")
            values.append(status)

        if updates:
            query = "UPDATE FEE SET " + ", ".join(updates) + " WHERE FeeID = %s"
            values.append(fee_id)
            cursor.execute(query, tuple(values))
            conn.commit()
            print("Fee record updated successfully.")
        else:
            print("No fields to update.")
    except Exception as e:
        print("Error updating fee record:", e)
    finally:
        cursor.close()
        conn.close()

# Function to delete a fee record by FeeID
def delete_fee(fee_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM FEE WHERE FeeID = %s", (fee_id,))
        conn.commit()
        print("Fee record deleted successfully.")
    except Exception as e:
        print("Error deleting fee record:", e)
    finally:
        cursor.close()
        conn.close()
