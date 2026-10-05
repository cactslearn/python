# Context Manager Example

# Open a file using a context manager
with open("example.txt", "w") as file:
    file.write("Hello, Python!")

print("File has been written successfully.")

# The file is automatically closed after the 'with' block
print("The file is automatically closed.")