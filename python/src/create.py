# create.py
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

    # Step 1: Create the student_scores table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student_scores (
            student_id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            score INTEGER
        );
    """)
    print("Table 'student_scores' created successfully or already exists.")

    # Commit the transaction to make sure changes are saved
    conn.commit()

    # Close cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
