# --- HASHMAP EXAMPLE ---
# Hashmaps store data in key-value pairs. They use a hash function 
# to compute an index where the value is stored, allowing lightning-fast lookups.
# In Python, hashmaps are implemented using built-in dictionaries (`dict`).

def hashmap_example():
    print("=== Hashmap (Dictionary) Example ===")
    
    # Creating a hashmap with key-value pairs
    # Keys must be unique and immutable (like strings or numbers).
    student_grades = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78
    }
    print(f"Initial Hashmap: {student_grades}")
    
    # 1. Fast lookup by key (O(1) average time complexity)
    # The key is passed through a hash function to instantly locate the value,
    # rather than searching through elements one by one.
    print(f"Bob's grade (lookup by key 'Bob'): {student_grades['Bob']}")
    
    # 2. Inserting a new key-value pair
    student_grades["Diana"] = 95
    print(f"After adding Diana: {student_grades}")
    
    # 3. Updating an existing value
    student_grades["Alice"] = 88
    print(f"After updating Alice's grade: {student_grades}")
    
    # 4. Deleting a key-value pair
    del student_grades["Charlie"]
    print(f"After deleting Charlie: {student_grades}\n")


# --- MAIN FUNCTION ---
if __name__ == "__main__":
    hashmap_example()