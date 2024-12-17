# library_example_usage.py
from library_query import get_books_by_author

# List of authors (as you have 6 authors, we will hard-code them)
authors = [
    "J.K. Rowling",
    "George Orwell",
    "J.R.R. Tolkien",
    "Agatha Christie",
    "Isaac Asimov",
    "Mark Twain"
]

# Loop over the authors and print their books
for author in authors:
    books = get_books_by_author(author)
    
    if books:
        print(f"Books by {author}:")
        for book in books:
            print(f"- {book}")
    else:
        print(f"No books found for {author}.")
    print("\n" + "-"*40 + "\n")  # Separator between authors
