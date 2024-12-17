# library_add.py
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

    # Insert authors
    cur.execute("""
        INSERT INTO Authors (name, birth_date) VALUES
        ('J.K. Rowling', '1965-07-31'),
        ('George Orwell', '1903-06-25'),
        ('J.R.R. Tolkien', '1892-01-03'),
        ('Agatha Christie', '1890-09-15'),
        ('Isaac Asimov', '1920-01-02'),
        ('Mark Twain', '1835-11-30'),
        ('F. Scott Fitzgerald', '1896-09-24')
        ON CONFLICT (name) DO NOTHING;
    """)

    # Insert books and associate them with authors
    cur.execute("""
        INSERT INTO Books (title, publisher, publication_year, isbn, author_id) VALUES
        ('Harry Potter and the Sorcerer''s Stone', 'Bloomsbury', 1997, '978-0747532699', 1),
        ('1984', 'Secker & Warburg', 1949, '978-0451524935', 2),
        ('The Hobbit', 'George Allen & Unwin', 1937, '978-0618968633', 3),
        ('Murder on the Orient Express', 'Collins Crime Club', 1934, '978-0007119318', 4),
        ('Foundation', 'Gnome Press', 1951, '978-0553293357', 5),
        ('The Adventures of Tom Sawyer', 'Chatto & Windus', 1876, '978-0143039563', 6),
        ('The Great Gatsby', 'Charles Scribner’s Sons', 1925, '978-0743273565', 7)
        ON CONFLICT (isbn) DO NOTHING;
    """)

    # Insert into Library table (linking authors to a list of books)
    cur.execute("""
        INSERT INTO Library (author_id, books) VALUES
        (1, ARRAY['Harry Potter and the Sorcerer''s Stone']),
        (2, ARRAY['1984']),
        (3, ARRAY['The Hobbit']),
        (4, ARRAY['Murder on the Orient Express']),
        (5, ARRAY['Foundation']),
        (6, ARRAY['The Adventures of Tom Sawyer']),
        (7, ARRAY['The Great Gatsby']);
    """)

    # Commit the transaction to ensure data is saved
    conn.commit()
    print("Data inserted successfully.")

    # Close cursor and connection
    cur.close()
    conn.close()

except Exception as e:
    print("An error occurred:", e)
