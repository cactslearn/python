def main():
    print("--- Python List Operations ---\n")

    # 1. Initialization
    fruits = ["apple", "banana", "cherry"]
    print(f"Initial list: {fruits}")

    # 2. Appending and Inserting
    fruits.append("orange")    # Adds to the end
    fruits.insert(1, "`mango`")  # Inserts at index 1
    print(f"After modifications: {fruits}")

    # 3. Accessing and Slicing
    print(f"Second element: {fruits[1]}")
    print(f"Slice (index 2 to 3): {fruits[2:4]}")

    # 4. Removing items
    fruits.remove("banana")  # Removes by value
    popped = fruits.pop(2)    # Removes by index and returns the item
    print(f"Removed '{popped}', current list: {fruits}")

    # 5. Iteration
    print("Listing all fruits:")
    for fruit in fruits:
        print(f" - {fruit}")

    # 6. Sorting and Reversing
    numbers = [5, 1, 8, 3]
    numbers.sort()
    print(f"\nSorted numbers: {numbers}")
    numbers.reverse()
    print(f"Reversed numbers: {numbers}")

if __name__ == "__main__":
    main()