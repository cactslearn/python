def greet(name, greeting="Hello"):
    """This function takes a name and an optional greeting."""
    return f"{greeting}, {name}!"

def calculate_sum(a, b):
    """This function performs a calculation and returns the result."""
    return a + b

def withdraw(atm_card, pin, amount = 500):
    return amount

def main():
    print("--- Function Demonstration ---\n")

    # Calling a function with positional arguments
    message = greet("Alice")
    print(message)
    print(greet("Pranav"))

    # Calling a function with a default argument override
    custom_msg = greet("Bob", "Good morning")
    print(custom_msg)

    # Using return values
    num1, num2 = 10, 25
    total = calculate_sum(num1, num2)
    print(f"The sum of {num1} and {num2} is: {total}")

    # Demonstrating local vs global scope
    # Variables defined inside a function (like 'message') cannot be accessed outside it.
    money = withdraw("MasterCard", "1234")
    print(f"Money Withdrawal: {money}")
    
if __name__ == "__main__":
    main()