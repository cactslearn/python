x = 10          # Global variable

def my_function():
    # global x
    x = 20      # Local variable
    print("Inside:", x)

my_function()

print("Outside:", x)