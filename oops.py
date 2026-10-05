class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(self.brand, "car is starting")


# Creating an object
car1 = Car("Toyota", "Red")

print(car1.brand)
print(car1.color)

car1.start()