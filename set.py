def main():
    print("--- Python Set Operations ---\n")

    # 1. Initialization
    # Sets use curly braces {}
    my_set = {1, 2, 3, 4, 4, 4}  # Duplicates are automatically removed
    print(f"Initial set (duplicates removed): {my_set}")

    # 2. Adding and Removing elements
    my_set.add(5)
    my_set.discard(2)  # Removes 2 if it exists; no error if it doesn't
    print(f"After adding 5 and removing 2: {my_set}")

    # 3. Membership Testing
    # Checking for an item in a set is extremely fast
    is_present = 3 in my_set
    print(f"Is 3 in the set? {is_present}")

    # 4. Set Mathematical Operations
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    
    print(f"\nSet A: {set_a}, Set B: {set_b}")
    print(f"Union (A | B): {set_a | set_b}")           # Combine all
    print(f"Intersection (A & B): {set_a & set_b}")    # Only common elements
    print(f"Difference (A - B): {set_b - set_a}")      # Items in A but not in B

    # 5. Clearing
    my_set.clear()
    print(f"Set after clearing: {my_set}")

if __name__ == "__main__":
    main()