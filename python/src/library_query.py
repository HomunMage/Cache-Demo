# library_query.py
import psycopg2
import os

# Get database connection details from environment variables
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

def get_books_by_author(author_name):
    """
    Queries the database to retrieve books written by a specific author.
    
    :param author_name: The name of the author whose books are to be retrieved.
    :return: A list of book titles by the specified author.
    """
    books = []
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host
        )
        # Create a cursor object
        cur = conn.cursor()

        # Query to fetch the books of a specific author
        query = """
            SELECT b.title
            FROM Books b
            JOIN Authors a ON b.author_id = a.author_id
            WHERE a.name = %s;
        """
        cur.execute(query, (author_name,))

        # Fetch results
        books = cur.fetchall()

        # Close cursor and connection
        cur.close()
        conn.close()

    except Exception as e:
        print("An error occurred:", e)

    return [book[0] for book in books]  # Return a list of book titles

# Example Usage: You can import this function in other files to use.
