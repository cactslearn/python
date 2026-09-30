def main():
    print("--- Python Dictionary Operations ---\n")

    # 1. Initialization
    # Keys must be immutable (strings, numbers, or tuples)
    user = {
        "name": "Alice",
        "age": 28,
        "role": "Developer"
    }
    print(f"Initial dictionary: {user}")

    # 2. Accessing and Modifying
    print(f"User name: {user['name']}")
    user["age"] = 29          # Update existing value
    user["city"] = "Pune"     # Add new key-value pair
    print(f"Updated dictionary: {user}")

    # 3. Safe Access
    # Using .get() prevents KeyError if the key doesn't exist
    print(f"Department: {user.get('department', 'Not assigned')}")

    # 4. Removing items
    removed_value = user.pop("role")
    print(f"Removed '{removed_value}', dictionary now: {user}")

    # 5. Iteration
    print("\nIterating through keys and values:")
    for key, value in user.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()