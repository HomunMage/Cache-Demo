# library_query.py
import psycopg2
import os

# Get database connection details from environment variables
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

def get_books_by_author(author_name):
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

        # If books found
        if books:
            print(f"Books by {author_name}:")
            for book in books:
                print(f"- {book[0]}")
        else:
            print(f"No books found for {author_name}.")

        # Close cursor and connection
        cur.close()
        conn.close()

    except Exception as e:
        print("An error occurred:", e)

# Example Usage (you can call this function elsewhere in your code)
if __name__ == "__main__":
    get_books_by_author("J.K. Rowling")
