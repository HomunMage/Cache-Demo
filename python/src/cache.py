# cache.py
from collections import OrderedDict

class Cache:
    def __init__(self, N):
        """
        Initializes the Cache with size limit N.
        N: The maximum size of the LRU cache and temp buffer.
        """
        self.N = N  # Cache size
        self.lru_cache = OrderedDict()  # The actual LRU cache, stores <key, value>
        self.temp_buffer = OrderedDict()  # Temporary buffer, stores <key, None>

    def _move_to_lru_cache(self, key, value):
        """Move an item from the temp buffer to the LRU cache."""
        if len(self.lru_cache) >= self.N:
            # If LRU cache is full, evict the least recently used item
            self.lru_cache.popitem(last=False)
        # Move the item to the LRU cache
        self.lru_cache[key] = value

    def fetch(self, key, fetch_function=None):
        """
        Fetches the value for a key. If not in the LRU cache, check the temporary buffer.
        If it's in the temp buffer and accessed consecutively more than once, move it to the LRU cache.
        """
        # Step 1: Check the LRU cache
        if key in self.lru_cache:
            # If the key is in the LRU cache, it's a cache hit
            # Move it to the front (most recently used)
            self.lru_cache.move_to_end(key)
            return self.lru_cache[key]
        
        # Step 2: If not found in LRU cache, check the temp buffer
        if key in self.temp_buffer:
            # The key was accessed once already, now fetch from the source and move to LRU
            if fetch_function:
                value = fetch_function(key)
                self._move_to_lru_cache(key, value)
                # Once moved to LRU, we don't need the key in the temp buffer anymore
                del self.temp_buffer[key]
                return value
        else:
            # Step 3: If key is not in either, fetch the data (e.g., from database)
            if fetch_function:
                value = fetch_function(key)
                # Add it to the temp buffer
                self.temp_buffer[key] = None  # Placeholder, we don't need value here
                # If the temp buffer exceeds size N, evict the least recently used item
                if len(self.temp_buffer) > 1:
                    self.temp_buffer.popitem(last=False)
                return value
            else:
                # If no fetch function is provided, return None or raise an error
                return None

    def __str__(self):
        """Helper function to show the current state of the cache"""
        return f"LRU Cache: {self.lru_cache}\nTemp Buffer: {self.temp_buffer}"
