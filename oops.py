class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(self.brand, "car is starting")


# Creating an object
car1 = Car("Toyota", "Red")
car1.color="Green"
print(car1.brand)
print(car1.color)
car1.start()

# Encapuslation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
            self.__balance = balance

account1 = BankAccount(100000)
# account1.set_balance(50000)
# print(account1.__balance)
print(account1.get_balance())

# Inheritance
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
     pass

# Dog().speak()
dog1 = Dog()
dog1.speak()

# Polymorphism
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

for animal in [Dog(), Cat()]:
    animal.speak()

# Abstraction
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        # print("Super mechanics of Payments")
        pass

class UPI(Payment):
    def pay(self):
        print("Payment using UPI")

payment = UPI()
payment.pay()