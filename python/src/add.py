# add.py
import psycopg2
import os

# Get database connection details from environment variables
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# Connect to PostgreSQL database
try:
    # Connect to the database
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host
    )
    print("Connected to the database successfully!")

    # Create a cursor object
    cur = conn.cursor()

    # Step 2: Insert two student records
    cur.execute("""
        INSERT INTO student_scores (name, score)
        VALUES
        ('Alice', 85),
        ('Bob', 92);
    """)
    print("Two student records inserted successfully.")

    # Commit the transaction to ensure data is saved
    conn.commit()

    # Step 3: Fetch and print the student records
    cur.execute("SELECT * FROM student_scores;")
    students = cur.fetchall()
    print("Student Scores:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Score: {student[2]}")

    # Close cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
