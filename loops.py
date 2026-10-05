print("Numbers 1 to 5")

for number in range(1, 6):
    print(f"Print next number {number}")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

count = 1
while count <= 4:
    print(f"Count is {count}")
    count += 1
print(f"Count is added next value {count}")

for letter in "Python":
    print(letter)

count = 1
while count <= 4:
    print(f"Count is {count}")
    count += 1
    if count == 2:
        break
print(f"Count after break {count}")

count = 0
while count <= 4: 
    count += 1       
    if count == 4:
        continue
    print(f"Count is {count}")        
print(f"Count after continue {count}")

