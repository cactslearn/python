numbers = [1, 2, 3, 4, 5]

# Using a normal for loop
squares = []

for number in numbers:
    squares.append(number * number)

print("Using for loop:", squares)


# Using list comprehension
c_squares = [number * number for number in numbers]

print("Using list comprehension:", c_squares)