import sys

def great_user(name):
    if not name.strip():
        raise ValueError("Name cannot be empty")
    match name:
        case "Samarth":
            return f"Hello, Samath Mhetre! Welcome to Python."
        case _:
            return f"Hello, {name.title()}! Welcome to Python."

def main():
    try:
        user_name = input("Enter your name to test:")
        greeting = great_user(user_name)
        print(greeting)
    except ValueError as e:
        print(f"\n[ERROR] Test failed: {e}")
    except KeyboardInterrupt:
        print("\n\n[INFO] Test cancelled by user.")

if __name__ == "__main__":
    main()