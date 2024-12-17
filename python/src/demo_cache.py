# demo_cache.py
import time
from cache import Cache
from library_query import get_books_by_author

# Create an instance of the cache with size N=3
cache = Cache(N=3)


# Function to simulate database/API fetching (for example usage)
def fetch_books(author):
    # Simulate the book fetching process by using the get_books_by_author function
    return get_books_by_author(author)

# Time fetching without cache
start_time_no_cache = time.time()
for _ in range(100):
    books = fetch_books("J.R.R. Tolkien")  # Simulate fetching without cache
end_time_no_cache = time.time()

# Time fetching with cache
start_time_with_cache = time.time()
for _ in range(100):
    books = cache.fetch("J.R.R. Tolkien", fetch_books)  # Fetch with cache
end_time_with_cache = time.time()

# Calculate the time differences
time_no_cache = end_time_no_cache - start_time_no_cache
time_with_cache = end_time_with_cache - start_time_with_cache

# Output the results
print(f"Time taken without cache (100 fetches): {time_no_cache:.6f} seconds")
print(f"Time taken with cache (100 fetches): {time_with_cache:.6f} seconds")
