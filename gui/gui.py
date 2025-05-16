import streamlit as st
import pandas as pd
from datetime import date
from calendar import monthrange
from db_config import get_connection
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db_config import get_connection


def run_query(query, params=None, fetch=False):
    conn=get_connection()
    cursor=conn.cursor()
    try:
        cursor.execute(query, params or ())
        if fetch:
            return cursor.fetchall()
        conn.commit()
    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()


# ------------------ COURSE ------------------
def course_section():
    st.subheader("Course Management")

    tab1, tab2, tab3, tab4=st.tabs(["Add", "View", "Update", "Delete"])

    with tab1:
        course_id=st.number_input("Course ID", step=1)
        name=st.text_input("Course Name")
        credits=st.number_input("Credits", step=1)
        dept=st.text_input("Department")
        if st.button("Add Course"):
            run_query("INSERT INTO COURSE (CourseID, CourseName, Credits, Department) VALUES (%s, %s, %s, %s)",
                      (course_id, name, credits, dept))
            st.success("Course added.")

    with tab2:
        rows=run_query("SELECT * FROM COURSE", fetch=True)
        st.dataframe(rows, use_container_width=True)

    with tab3:
        course_id=st.number_input("Enter Course ID to update", step=1)
        name=st.text_input("New Course Name")
        credits=st.number_input("New Credits", step=1)
        dept=st.text_input("New Department")
        if st.button("Update Course"):
            run_query("UPDATE COURSE SET CourseName=%s, Credits=%s, Department=%s WHERE CourseID=%s",
                      (name, credits, dept, course_id))
            st.success("Course updated.")

    with tab4:
        course_id=st.number_input("Enter Course ID to delete", step=1)
        if st.button("Delete Course"):
            run_query("DELETE FROM COURSE WHERE CourseID=%s", (course_id,))
            st.success("Course deleted.")


# ------------------ MARKS ------------------
def marks_section():
    st.subheader("Marks Management")

    tab1, tab2, tab3, tab4=st.tabs(["Add", "View", "Update", "Delete"])

    with tab1:
        sid=st.number_input("Student ID", step=1)
        cid=st.number_input("Course ID", step=1)
        marks=st.number_input("Marks Obtained")
        if st.button("Add Marks"):
            run_query("INSERT INTO MARKS (StudentID, CourseID, MarksObtained) VALUES (%s, %s, %s)",
                      (sid, cid, marks))
            st.success("Marks added.")

    with tab2:
        rows=run_query("SELECT * FROM MARKS", fetch=True)
        st.dataframe(rows, use_container_width=True)

    with tab3:
        mid=st.number_input("Enter Mark ID to update", step=1)
        marks=st.number_input("New Marks Obtained")
        if st.button("Update Marks"):
            run_query("UPDATE MARKS SET MarksObtained=%s WHERE MarkID=%s", (marks, mid))
            st.success("Marks updated.")

    with tab4:
        mid=st.number_input("Enter Mark ID to delete", step=1)
        if st.button("Delete Marks"):
            run_query("DELETE FROM MARKS WHERE MarkID=%s", (mid,))
            st.success("Marks deleted.")


# ------------------ ATTENDANCE ------------------
def attendance_section():
    st.subheader("Attendance Management")

    tab1, tab2, tab3, tab4=st.tabs(["Add", "View", "Update", "Delete"])

    with tab1:
        sid=st.number_input("Student ID", step=1)
        cid=st.number_input("Course ID", step=1)
        date=st.date_input("Date")
        status=st.selectbox("Status", ["Present", "Absent"])
        if st.button("Add Attendance"):
            run_query("INSERT INTO ATTENDANCE (StudentID, CourseID, Date, Status) VALUES (%s, %s, %s, %s)",
                      (sid, cid, date, status))
            st.success("Attendance added.")

    with tab2:
        rows=run_query("SELECT * FROM ATTENDANCE", fetch=True)
        st.dataframe(rows, use_container_width=True)

    with tab3:
        aid=st.number_input("Enter Attendance ID to update", step=1)
        status=st.selectbox("New Status", ["Present", "Absent"])
        if st.button("Update Attendance"):
            run_query("UPDATE ATTENDANCE SET Status=%s WHERE AttendanceID=%s", (status, aid))
            st.success("Attendance updated.")

    with tab4:
        aid=st.number_input("Enter Attendance ID to delete", step=1)
        if st.button("Delete Attendance"):
            run_query("DELETE FROM ATTENDANCE WHERE AttendanceID=%s", (aid,))
            st.success("Attendance deleted.")


# ------------------ FEE ------------------
def fee_section():
    st.subheader("Fee Management")

    tab1, tab2, tab3, tab4=st.tabs(["Add", "View", "Update", "Delete"])

    with tab1:
        sid=st.number_input("Student ID", step=1)
        amt=st.number_input("Amount", step=1)
        date=st.date_input("Paid Date")
        status=st.selectbox("Status", ["Paid", "Unpaid"])
        if st.button("Add Fee"):
            run_query("INSERT INTO FEE (StudentID, Amount, PaidDate, Status) VALUES (%s, %s, %s, %s)",
                      (sid, amt, date, status))
            st.success("Fee record added.")

    with tab2:
        rows=run_query("SELECT * FROM FEE", fetch=True)
        st.dataframe(rows, use_container_width=True)

    with tab3:
        fid=st.number_input("Enter Fee ID to update", step=1)
        status=st.selectbox("New Status", ["Paid", "Unpaid"])
        if st.button("Update Fee"):
            run_query("UPDATE FEE SET Status=%s WHERE FeeID=%s", (status, fid))
            st.success("Fee updated.")

    with tab4:
        fid=st.number_input("Enter Fee ID to delete", step=1)
        if st.button("Delete Fee"):
            run_query("DELETE FROM FEE WHERE FeeID=%s", (fid,))
            st.success("Fee record deleted.")


# ------------------ STUDENT ------------------
def student_section():
    st.subheader("Student Management")

    tab1, tab2, tab3, tab4=st.tabs(["Add", "View", "Update", "Delete"])

    with tab1:
        student_id=st.number_input("Student ID", step=1)
        name=st.text_input("Student Name")
        dob=st.date_input("Date of Birth")
        gender=st.selectbox("Gender", ["Male", "Female", "Other"])
        if st.button("Add Student"):
            run_query(
                "INSERT INTO STUDENT (StudentID, Name, DOB, Gender) VALUES (%s, %s, %s, %s)",
                (student_id, name, dob, gender)
            )
            st.success("Student added.")

    with tab2:
        rows=run_query("SELECT * FROM STUDENT", fetch=True)
        st.dataframe(rows, use_container_width=True)

    with tab3:
        student_id=st.number_input("Enter Student ID to update", step=1)
        name=st.text_input("New Student Name")
        dob=st.date_input("New Date of Birth")
        gender=st.selectbox("New Gender", ["Male", "Female", "Other"])
        if st.button("Update Student"):
            run_query(
                "UPDATE STUDENT SET Name=%s, DOB=%s, Gender=%s WHERE StudentID=%s",
                (name, dob, gender, student_id)
            )
            st.success("Student updated.")

    with tab4:
        student_id=st.number_input("Enter Student ID to delete", step=1)
        if st.button("Delete Student"):
            run_query("DELETE FROM STUDENT WHERE StudentID=%s", (student_id,))
            st.success("Student deleted.")

# ------------------ REPORTS ------------------
def reports_section():
    st.subheader("Reports & Aggregations")

    report_options={
        "Student Marks Summary": """
            SELECT s.StudentID, s.Name, c.CourseName, m.MarksObtained
            FROM STUDENT s
            JOIN MARKS m ON s.StudentID=m.StudentID
            JOIN COURSE c ON m.CourseID=c.CourseID
            ORDER BY s.StudentID, c.CourseName
        """,
        "Average Marks per Course": """
            SELECT c.CourseName, AVG(m.MarksObtained) AS AverageMarks
            FROM MARKS m
            JOIN COURSE c ON m.CourseID=c.CourseID
            GROUP BY c.CourseName
            ORDER BY AverageMarks DESC
        """,
        "Attendance Percentage per Student": """
            SELECT s.StudentID, s.Name,
                   ROUND(100.0 * SUM(CASE WHEN a.Status='Present' THEN 1 ELSE 0 END) / COUNT(*), 2) AS AttendancePercentage
            FROM STUDENT s
            JOIN ATTENDANCE a ON s.StudentID=a.StudentID
            GROUP BY s.StudentID, s.Name
            ORDER BY AttendancePercentage DESC
        """,
        "Fee Payment Status Summary": """
            SELECT s.StudentID, s.Name,
                   SUM(f.Amount) AS TotalFees,
                   SUM(CASE WHEN f.Status='Paid' THEN f.Amount ELSE 0 END) AS PaidAmount,
                   SUM(CASE WHEN f.Status='Unpaid' THEN f.Amount ELSE 0 END) AS UnpaidAmount
            FROM STUDENT s
            LEFT JOIN FEE f ON s.StudentID=f.StudentID
            GROUP BY s.StudentID, s.Name
            ORDER BY s.StudentID
        """
    }

    selected_report=st.selectbox("Select Report", list(report_options.keys()))

    if st.button("Run Report"):
        query=report_options[selected_report]
        rows=run_query(query, fetch=True)
        if rows:
            st.dataframe(rows, use_container_width=True)
        else:
            st.info("No data available for this report.")

def performance_analysis_section():
    st.subheader("Student Performance Analysis")

    courses=run_query("SELECT CourseID, CourseName FROM COURSE", fetch=True)
    course_dict={c[1]: c[0] for c in courses}

    selected_course=st.selectbox("Select Course", list(course_dict.keys()))
    if st.button("Show Marks Distribution"):
        course_id=course_dict[selected_course]
        query="""
            SELECT s.Name, m.MarksObtained
            FROM MARKS m
            JOIN STUDENT s ON m.StudentID=s.StudentID
            WHERE m.CourseID=%s
        """
        data=run_query(query, (course_id,), fetch=True)
        if data:
            names=[row[0] for row in data]
            marks=[row[1] for row in data]

            import pandas as pd
            df=pd.DataFrame({"Student": names, "Marks": marks})
            st.bar_chart(df.set_index("Student"))
        else:
            st.info("No marks data found for selected course.")


def upcoming_birthdays_section():
    st.subheader("Upcoming Student Birthdays")

    days_ahead=st.slider("Select days ahead", 1, 30, 7)

    query="""
        SELECT StudentID, Name, DOB
        FROM STUDENT
    """
    rows=run_query(query, fetch=True)

    import datetime
    today=datetime.date.today()
    upcoming=[]
    for sid, name, dob in rows:
        birthday_this_year=dob.replace(year=today.year)
        delta=(birthday_this_year - today).days
        if 0 <= delta <= days_ahead:
            upcoming.append((sid, name, dob.strftime("%Y-%m-%d")))

    if upcoming:
        st.table(upcoming)
    else:
        st.info(f"No birthdays in next {days_ahead} days.")


def enrollment_summary_section():
    st.subheader("Course Enrollment Summary")

    query="""
        SELECT c.CourseName, COUNT(DISTINCT m.StudentID) AS EnrolledStudents
        FROM COURSE c
        LEFT JOIN MARKS m ON c.CourseID=m.CourseID
        GROUP BY c.CourseName
        ORDER BY EnrolledStudents DESC
    """
    rows=run_query(query, fetch=True)
    if rows:
        import pandas as pd
        df=pd.DataFrame(rows, columns=["Course Name", "Enrolled Students"])
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No enrollment data available.")

def attendance_summary_section():
    st.subheader("Attendance Summary")

    start_date=st.date_input("Start Date")
    end_date=st.date_input("End Date")
    if start_date > end_date:
        st.error("Start Date must be before End Date.")
        return

    query="""
        SELECT s.StudentID, s.Name, c.CourseName,
            ROUND(100.0 * SUM(CASE WHEN a.Status='Present' THEN 1 ELSE 0 END) / COUNT(*), 2) AS AttendancePercent
        FROM ATTENDANCE a
        JOIN STUDENT s ON a.StudentID=s.StudentID
        JOIN COURSE c ON a.CourseID=c.CourseID
        WHERE a.Date BETWEEN %s AND %s
        GROUP BY s.StudentID, s.Name, c.CourseName
        ORDER BY AttendancePercent ASC
    """
    rows=run_query(query, (start_date, end_date), fetch=True)

    if rows:
        import pandas as pd
        df=pd.DataFrame(rows, columns=["Student ID", "Name", "Course", "Attendance %"])
        st.dataframe(df)
        
        low_attendance=df[df["Attendance %"] < 75]
        if not low_attendance.empty:
            st.warning("Students with attendance below 75%:")
            st.dataframe(low_attendance)
    else:
        st.info("No attendance records found for the selected period.")


def fee_payment_summary_section():
    st.subheader("Fee Payment Summary")

    status_filter=st.selectbox("Filter by Status", ["All", "Paid", "Unpaid"])
    
    base_query="""
        SELECT s.StudentID, s.Name, SUM(f.Amount) as TotalFees, 
               SUM(CASE WHEN f.Status='Paid' THEN f.Amount ELSE 0 END) as PaidAmount,
               SUM(CASE WHEN f.Status='Unpaid' THEN f.Amount ELSE 0 END) as UnpaidAmount
        FROM FEE f
        JOIN STUDENT s ON f.StudentID=s.StudentID
    """
    where_clause=""
    params=()

    if status_filter != "All":
        where_clause=" WHERE f.Status=%s"
        params=(status_filter,)

    query=base_query + where_clause + " GROUP BY s.StudentID, s.Name ORDER BY UnpaidAmount DESC"
    rows=run_query(query, params, fetch=True)

    if rows:
        import pandas as pd
        df=pd.DataFrame(rows, columns=["Student ID", "Name", "Total Fees", "Paid Amount", "Unpaid Amount"])
        st.dataframe(df)
        if status_filter != "All" and len(df) == 0:
            st.info(f"No students found with {status_filter} fees.")
    else:
        st.info("No fee records found.")


def student_profile_section():
    st.subheader("Student Profile")

    students=run_query("SELECT StudentID, Name FROM STUDENT", fetch=True)
    student_dict={f"{s[1]} ({s[0]})": s[0] for s in students}

    selected=st.selectbox("Select Student", list(student_dict.keys()))
    if selected:
        student_id=student_dict[selected]
        # Personal info
        info=run_query("SELECT * FROM STUDENT WHERE StudentID=%s", (student_id,), fetch=True)
        st.markdown("**Personal Information:**")
        st.write(info[0])

        # Marks
        marks=run_query("""
            SELECT c.CourseName, m.MarksObtained
            FROM MARKS m
            JOIN COURSE c ON m.CourseID=c.CourseID
            WHERE m.StudentID=%s
        """, (student_id,), fetch=True)
        st.markdown("**Marks:**")
        st.dataframe(marks)

        # Attendance summary
        attendance=run_query("""
            SELECT c.CourseName,
                   ROUND(100.0 * SUM(CASE WHEN a.Status='Present' THEN 1 ELSE 0 END) / COUNT(*), 2) AS AttendancePercent
            FROM ATTENDANCE a
            JOIN COURSE c ON a.CourseID=c.CourseID
            WHERE a.StudentID=%s
            GROUP BY c.CourseName
        """, (student_id,), fetch=True)
        st.markdown("**Attendance % per Course:**")
        st.dataframe(attendance)

        # Fee summary
        fee=run_query("""
            SELECT SUM(Amount) as TotalFees, 
                   SUM(CASE WHEN Status='Paid' THEN Amount ELSE 0 END) as PaidAmount,
                   SUM(CASE WHEN Status='Unpaid' THEN Amount ELSE 0 END) as UnpaidAmount
            FROM FEE
            WHERE StudentID=%s
        """, (student_id,), fetch=True)
        st.markdown("**Fee Summary:**")
        st.write(fee[0])

def custom_query_section():
    st.subheader("Run Custom Query (Read-Only)")

    query=st.text_area("Write your SELECT query here (must be SELECT only):")
    if st.button("Run Query"):
        if query.strip().lower().startswith("select"):
            try:
                result=run_query(query, fetch=True)
                if result:
                    import pandas as pd
                    df=pd.DataFrame(result)
                    st.dataframe(df)
                else:
                    st.info("Query ran successfully but returned no data.")
            except Exception as e:
                st.error(f"Error running query: {e}")
        else:
            st.error("Only SELECT queries are allowed.")


def dashboard_section():
    st.header("🧮 Dashboard Overview")

    conn=get_connection()
    cursor=conn.cursor()

    # --- Total Students ---
    cursor.execute("SELECT COUNT(*) FROM STUDENT")
    total_students=cursor.fetchone()[0]
    st.metric("👨‍🎓 Total Students", total_students)

    # --- Total Courses ---
    cursor.execute("SELECT COUNT(*) FROM COURSE")
    total_courses=cursor.fetchone()[0]
    st.metric("📘 Total Courses", total_courses)

    # --- Attendance % Today ---
    today=date.today()
    cursor.execute("SELECT COUNT(*) FROM ATTENDANCE WHERE Date=%s", (today,))
    total_today=cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM ATTENDANCE WHERE Date=%s AND Status='Present'", (today,))
    present_today=cursor.fetchone()[0]

    attendance_pct=(present_today / total_today) * 100 if total_today > 0 else 0
    st.metric("📅 Attendance % Today", f"{attendance_pct:.2f}%")

    # --- Fees Collected This Month ---
    first_day=today.replace(day=1)
    last_day=today.replace(day=monthrange(today.year, today.month)[1])

    cursor.execute("""
        SELECT SUM(Amount) FROM FEE 
        WHERE Status='Paid' AND PaidDate BETWEEN %s AND %s
    """, (first_day, last_day))
    fees_this_month=cursor.fetchone()[0] or 0.0
    st.metric("💰 Fees Collected This Month", f"${fees_this_month:.2f}")

    # --- Average Marks by Course ---
    st.subheader("📊 Average Marks by Course")
    query="""
        SELECT C.CourseName, AVG(M.MarksObtained) as AvgMarks
        FROM MARKS M
        JOIN COURSE C ON M.CourseID=C.CourseID
        GROUP BY C.CourseName
    """
    df_avg_marks=pd.read_sql(query, conn)
    st.dataframe(df_avg_marks)

    cursor.close()
    conn.close()


def student_insights_section():
    st.header("🧑‍🎓 Student Insights")

    subsection=st.selectbox("Choose Insight", [
        "Top Performers",
        "Low Performers",
        "Irregular Students",
        "Defaulters"
    ])

    conn=get_connection()

    if subsection == "Top Performers":
        st.subheader("🌟 Top Performers (Avg Marks > 90)")
        query="""
            SELECT S.StudentID, S.Name, AVG(M.MarksObtained) AS AverageMarks
            FROM STUDENT S
            JOIN MARKS M ON S.StudentID=M.StudentID
            GROUP BY S.StudentID, S.Name
            HAVING AVG(M.MarksObtained) > 90
            ORDER BY AverageMarks DESC
        """
        df=pd.read_sql(query, conn)
        st.dataframe(df)

    elif subsection == "Low Performers":
        st.subheader("🔻 Low Performers (Avg Marks < 40)")
        query="""
            SELECT S.StudentID, S.Name, AVG(M.MarksObtained) AS AverageMarks
            FROM STUDENT S
            JOIN MARKS M ON S.StudentID=M.StudentID
            GROUP BY S.StudentID, S.Name
            HAVING AVG(M.MarksObtained) < 40
            ORDER BY AverageMarks ASC
        """
        df=pd.read_sql(query, conn)
        st.dataframe(df)

    elif subsection == "Irregular Students":
        st.subheader("📉 Irregular Students (Attendance < 75%)")
        query="""
            SELECT S.StudentID, S.Name,
                   COUNT(A.AttendanceID) AS TotalDays,
                   SUM(CASE WHEN A.Status='Present' THEN 1 ELSE 0 END) AS PresentDays,
                   ROUND(100.0 * SUM(CASE WHEN A.Status='Present' THEN 1 ELSE 0 END) / COUNT(A.AttendanceID), 2) AS AttendancePercent
            FROM STUDENT S
            JOIN ATTENDANCE A ON S.StudentID=A.StudentID
            GROUP BY S.StudentID, S.Name
            HAVING AttendancePercent < 75
            ORDER BY AttendancePercent ASC
        """
        df=pd.read_sql(query, conn)
        st.dataframe(df)

    elif subsection == "Defaulters":
        st.subheader("💸 Fee Defaulters (Unpaid Fees)")
        query="""
            SELECT DISTINCT S.StudentID, S.Name, F.Status
            FROM STUDENT S
            JOIN FEE F ON S.StudentID=F.StudentID
            WHERE F.Status='Unpaid'
        """
        df=pd.read_sql(query, conn)
        st.dataframe(df)

    conn.close()

def academic_calendar_section():
    st.header("📅 Academic Calendar")

    conn=get_connection()
    
    subsection=st.sidebar.selectbox("Select Academic Calendar Insight", [
        #"Upcoming Tests/Exam Days",  # Removed due to no date in MARKS
        "Busy Days (High Attendance)",
        "Holidays/Zero Attendance Days"
    ])

    if subsection == "Busy Days (High Attendance)":
        st.subheader("Busy Days (High Attendance)")
        query="""
            SELECT Date, COUNT(*) AS PresentCount
            FROM ATTENDANCE
            WHERE Status='Present'
            GROUP BY Date
            ORDER BY PresentCount DESC
            LIMIT 10;
        """
        try:
            df=pd.read_sql(query, conn)
            if df.empty:
                st.info("No attendance data available.")
            else:
                st.table(df)
        except Exception as e:
            st.error(f"Error fetching busy attendance days: {e}")

    elif subsection == "Holidays/Zero Attendance Days":
        st.subheader("Holidays / Zero Attendance Days")
        import datetime
        date_today=datetime.date.today()
        start_date=date_today - datetime.timedelta(days=30)
        
        query=f"""
            SELECT Date, 
                   SUM(CASE WHEN Status='Present' THEN 1 ELSE 0 END) AS PresentCount
            FROM ATTENDANCE
            WHERE Date BETWEEN '{start_date}' AND '{date_today}'
            GROUP BY Date
            HAVING PresentCount=0
            ORDER BY Date ASC;
        """
        try:
            df=pd.read_sql(query, conn)
            if df.empty:
                st.info("No holidays or zero attendance days found in the last 30 days.")
            else:
                st.table(df)
        except Exception as e:
            st.error(f"Error fetching holidays/zero attendance days: {e}")

    conn.close()


# ------------------ MAIN APP ------------------
st.title("📚 School Management System")

main_menu=st.sidebar.radio("Choose Section", [
    "Dashboard", 
    "Core Modules", 
    "Analytics & Reports", 
    "Student Insights",
    "Academic Calendar"   
])

if main_menu == "Dashboard":
    dashboard_section()

elif main_menu == "Core Modules":
    core_menu=st.sidebar.radio("Select Core Module", [
        "Student", "Course", "Marks", "Attendance", "Fee"
    ])

    if core_menu == "Student":
        student_section()
    elif core_menu == "Course":
        course_section()
    elif core_menu == "Marks":
        marks_section()
    elif core_menu == "Attendance":
        attendance_section()
    elif core_menu == "Fee":
        fee_section()

elif main_menu == "Analytics & Reports":
    reports_menu=st.sidebar.radio("Select Report", [
        "Reports", "Performance Analysis", "Upcoming Birthdays", "Enrollment Summary",  
        "Attendance Summary", "Fee Payment Summary", "Student Profile", "Custom Query"
    ])

    if reports_menu == "Reports":
        reports_section()
    elif reports_menu == "Performance Analysis":
        performance_analysis_section()
    elif reports_menu == "Upcoming Birthdays":
        upcoming_birthdays_section()
    elif reports_menu == "Enrollment Summary":
        enrollment_summary_section()
    elif reports_menu == "Attendance Summary":
        attendance_summary_section()
    elif reports_menu == "Fee Payment Summary":
        fee_payment_summary_section()
    elif reports_menu == "Student Profile":
        student_profile_section()
    elif reports_menu == "Custom Query":
        custom_query_section()

elif main_menu == "Student Insights":
    student_insights_section()

elif main_menu == "Academic Calendar":
    academic_calendar_section() 
