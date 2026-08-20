# Import the built-in SQLite library to interact with SQL databases
import sqlite3

# Define the name of the database file
DB_NAME = "university.db"


def run_script(cursor, filepath):
    """
    Utility function to load and run an external .sql file.
    """
    # Open the SQL file in read mode
    with open(filepath, 'r') as file:
        # Read the entire SQL file
        sql_script = file.read()

    # Execute all SQL commands in the file
    cursor.executescript(sql_script)


def main():

    # Step 1: Connect to the database
    conn = sqlite3.connect(DB_NAME)

    # Create cursor
    cursor = conn.cursor()


    # Step 2: Set up the database tables
    print("Setting up database schema...")
    run_script(cursor, "schema.sql")


    # Step 3: Insert sample data
    print("Seeding initial data...")
    run_script(cursor, "seed.sql")

    # Save changes
    conn.commit()


    # Step 4: SQL Query 1
    # Question: How many students are registered in each course?

    print("\n=========================================")
    print("Q1: Registered Students Count Per Course")
    print("=========================================")

    q1_sql = """
    SELECT 
        s.SUBJECT_CODE,
        COUNT(e.STUDENT_NUM)
    FROM SUBJECTS s
    LEFT JOIN ENROLLMENT e
        ON s.SUBJECT_CODE = e.SUBJECT_CODE
    GROUP BY s.SUBJECT_CODE;
    """

    results_q1 = cursor.execute(q1_sql).fetchall()

    for course, count in results_q1:
        print(f"Course: {course:<10} | Enrolled: {count}")


    # Step 5: SQL Query 2
    # Question: List names and student IDs of students
    # enrolled in more than one course

    print("\n=========================================")
    print("Q2: Students Enrolled in >1 Course")
    print("=========================================")

    q2_sql = """
    SELECT
        s.NID,
        s.F_NAME || ' ' || s.L_NAME,
        COUNT(e.SUBJECT_CODE)
    FROM student s
    JOIN ENROLLMENT e
        ON s.NID = e.STUDENT_NUM
    GROUP BY s.NID, s.F_NAME, s.L_NAME
    HAVING COUNT(e.SUBJECT_CODE) > 1;
    """

    results_q2 = cursor.execute(q2_sql).fetchall()

    for student_id, name, count in results_q2:
        print(f"ID: {student_id} | Name: {name:<20} | Total Courses: {count}")


    # Step 6: Close the database connection
    conn.close()


# Run main() when this file is executed directly
if __name__ == "__main__":
    main()