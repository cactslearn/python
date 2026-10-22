# Context Manager Example

# Open a file using a context manager
with open("example.txt", "a") as file:
    file.write("Hello, Python Lets Append!")

print("File has been written successfully.")

# The file is automatically closed after the 'with' block
print("The file is automatically closed.")