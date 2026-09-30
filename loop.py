import sys

def main():
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"I like {fruit}")

    for i in range(5):
        print(f"Loop count {i+1}")

    count = 1
    while count <= 3:
        print(f"Count is {count}")
        count += 1

    print("Break")
    for num in range(10):
        if num == 5:
            break
        print(num)

    print("Continue")
    for num in range(1, 6):
        if num == 3:
            continue
        print(num)

    print("Pass")
    for num in range(5):
        if num == 2:
            pass
        print(num)

    print("for else")
    for fruit in fruits:
        if fruit == "orange":
            print("orange")
            break
    else:
        print("Fruit is not in the list.")

if __name__ == "__main__":
    main()