# library_create.py
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

    # Create the Authors table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Authors (
            author_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE,
            birth_date DATE
        );
    """)

    # Create the Books table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            book_id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            publisher VARCHAR(255),
            publication_year INT,
            isbn VARCHAR(20) UNIQUE,
            author_id INT,
            FOREIGN KEY (author_id) REFERENCES Authors(author_id)
        );
    """)

    # Create the Library table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Library (
            library_id SERIAL PRIMARY KEY,
            author_id INT,
            books TEXT[],
            FOREIGN KEY (author_id) REFERENCES Authors(author_id)
        );
    """)

    # Commit the transaction to create tables
    conn.commit()
    print("Library table and related tables created successfully.")

    # Close cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
