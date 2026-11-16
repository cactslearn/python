customers =[
    "  Jhon Smith   ",
    "  David-Jones   ",
    "  Jhon Rambo   "
]
print(customers)
cleaned_customers = []

for name in customers:
    name = name.strip()
    name = name.replace("-", " ")
    name = name.split()
    cleaned_customers.append(name)

print(cleaned_customers)