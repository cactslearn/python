# Generator Expression Example in Python

# Generator expression
numbers = (x * x for x in range(1, 6))

# numbers is a generator object
print("Generator object:")
print(numbers)

# Generate values one by one
print("\nValues:")
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

# Create another generator
numbers = (x * x for x in range(1, 6))

# Using a for loop to get values
print("\nUsing for loop:")
for value in numbers:
    print(value)

# Generator expressions are memory efficient
large_numbers = (x * x for x in range(1, 1000000))

print("\nLarge generator created successfully.")
print("First value:", next(large_numbers))
print("Second value:", next(large_numbers))
print("Third value:", next(large_numbers))

# Compare with a list comprehension
list_numbers = [x * x for x in range(1, 6)]

print("\nList comprehension:")
print(list_numbers)

# Generator expression
generator_numbers = (x * x for x in range(1, 6))

print("\nGenerator expression:")
for value in generator_numbers:
    print(value)