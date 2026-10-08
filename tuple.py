def main():
    print("--- Python Tuple Operations ---\n")

    # 1. Defining a Tuple (using parentheses)
    # Note: A single-item tuple must have a trailing comma
    coordinates = (10.5, 20.2)
    user_info = ("Alice", 25, "Engineer")
    single_item = (5,) 

    print(f"Coordinates: {coordinates}")
    print(f"User Info: {user_info}")

    # 2. Accessing elements (same as lists)
    print(f"Name: {user_info[0]}, Age: {user_info[1]}")

    # 3. Tuple Unpacking
    # Assigning tuple elements to individual variables
    name, age, job = user_info
    print(f"\nUnpacked variables -> Name: {name}, Job: {job}")

    # 4. Immutability Test
    # The following line would raise a TypeError:
    # user_info[1] = 26 
    print("\nNote: Tuples are immutable. Trying to change 'user_info[1] = 26' would cause an error.")

    # 5. Common Tuple Methods
    # Tuples only have two built-in methods: count() and index()
    my_tuple = (1, 2, 2, 2, 3, 4)
    print(f"Count of '2' in tuple: {my_tuple.count(2)}")
    print(f"Index of '3': {my_tuple.index(3)}")

if __name__ == "__main__":
    main()