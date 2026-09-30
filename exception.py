def main():
    print("--- Exception Handling Demonstration ---\n")
    
    # We will try to perform division based on user input
    numerator_input = input("Enter a numerator: ")
    denominator_input = input("Enter a denominator: ")

    try:
        # Attempt to convert strings to floats and perform division
        num = float(numerator_input)
        den = float(denominator_input)
        result = num / den
        
    except ValueError:
        # Triggered if input is not a number
        print("Error: Invalid input. Please enter numeric values.")
        
    except ZeroDivisionError:
        # Triggered if denominator is 0
        print("Error: You cannot divide by zero.")
        
    else:
        # Runs only if NO exceptions were raised
        print(f"Success! The result is: {result}")
        
    finally:
        # Always runs, regardless of whether an error occurred
        print("Execution complete. Cleaning up resources.")

if __name__ == "__main__":
    main()