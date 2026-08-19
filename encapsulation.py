#                               Encapsulation

# Encapsulation with Validation

class Product:
    def __init__(self, price):
        self.__price = price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price")

    def get_price(self):
        return self.__price

product = Product(500)
product.set_price(700)
print(product.get_price())

print("=========================")


# Practical Encapsulation

class Mobile:
    def __init__(self, battery):
        self.__battery = battery

    def charge(self, amount):
        self.__battery += amount
        if self.__battery > 100:
            self.__battery = 100

    def use(self, amount):
        if amount <= self.__battery:
            self.__battery -= amount
        else:
            print("Battery is low")

    def show_battery(self):
        print("Battery:", self.__battery, "%")

mobile = Mobile(50)
mobile.charge(30)
mobile.use(20)
mobile.show_battery()

print("=========================")


#                                Abstraction — 

# Abstract Animal Class

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog = Dog()
dog.sound()

print("=========================")

# Abstract Shape

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(10, 5)
print(rectangle.area())

print("=========================")

# Abstract Payment System

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")

p1 = CreditCard()
p2 = UPI()

p1.pay(1000)
p2.pay(500)

print("=========================")

# Abstract Employee

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary = ₹60,000")

class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary = ₹80,000")

d = Developer()
m = Manager()

d.calculate_salary()
m.calculate_salary()

print("=========================")

# Abstract Vehicle

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

car = Car()
car.start()
car.stop()

print("=========================")

#                    @classmethod and @staticmethod 
# Basic @classmethod

class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name

print(Student.school)
Student.change_school("XYZ School")
print(Student.school)

print("=========================")

# Class Method as Alternative Constructor

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))

student = Student.from_string("Vinay,21")

print(student.name)
print(student.age)

print("=========================")

# Basic @staticmethod

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))

print("=========================")

# Static Method for Validation

class User:
    @staticmethod
    def valid_email(email):
        return "@" in email

print(User.valid_email("abc@gmail.com"))
print(User.valid_email("abcgmail.com"))

print("=========================")

# Class Method + Static Method Together

class Bank:
    bank_name = "SBI"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    @staticmethod
    def validate_account(account_number):
        return len(str(account_number)) == 10

print(Bank.bank_name)
Bank.change_bank_name("HDFC")
print(Bank.bank_name)
print(Bank.validate_account(1234567890))