#                           POLYMORPHISM

# method overriding

class Animal:
    def sound(self):
        print("Animal make sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meow")

dog=Dog()
cat=Cat()

dog.sound()
cat.sound()
print("====================")

# polymorphism with different classes

class Car:
    def start(self):
        print("car start with a key ")

class Bike:
    def start(self):
        print("bike start with a button")

def start_vehicle(vehicle):
    vehicle.start()

car=Car()
bike=Bike()

start_vehicle(car)
start_vehicle(bike)
print("===================")

# polymorphism with same method name

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius *self.radius

r=Rectangle(10,20)
c=Circle(5)

print("Area Rectangle",r.area())
print("Area circle",c.area())
print("==================")

# polmorphism with inheritance

class Employee:
    def calculate_salary(self):
        print("Calculating Salary")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Salary = 20000")

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print("Salary = 15000")

employees={
    FullTimeEmployee(),
    PartTimeEmployee()
}

for employee in employees:
    employee.calculate_salary()

print("======================")


#                           Getter & Setter 

# Getter and Setter for Student marks

class Student:
    def __init__(self,marks):
        self.marks=marks

    def get_marks(self):
        return self.marks

    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks=marks
        else:
            print("Invalid Marks")

student=Student(80)
print(student.get_marks())
student.set_marks(90)
print(student.get_marks())

print("====================")

# Getter and Setter for Age

class Person:
    def __init__(self,age):
        self.age=age

    def get_age(self):
        return self.age

    def set_age(self,age):
        if age>=0:
            self.__age=age
        else:
            print("Age cannot be negative")

person=Person(23)
print(person.get_age())
person.set_age(25)
print(person.get_age())

print("===========================")

# Using @property

class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,amount):
        if amount>=0:
            self.__balance=amount
        else:
            print("Balance cannot be negative")

account=BankAccount(5000)
print(account.balance)
account.balance=8000
print(account.balance)

print("======================")

# Validate Salary

class Employee:
    def __init__(self,salary):
        self.salary=salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary):
        if salary>=1000:
            self.__salary=salary
        else:
            print("Salary must be at least Rs 10000")

employee=Employee(25000)
print(employee.salary)
employee.salary=30000
print(employee.salary)
print("====================")

# Getter/Setter for Password

class User:
    def __init__(self, password):
        self.__password = password

    @property
    def password(self):
        return "Password is hidden"

    @password.setter
    def password(self, password):
        if len(password) >= 8:
            self.__password = password
            print("Password updated")
        else:
            print("Password must contain at least 8 characters")

user = User("abc12345")
print(user.password)
user.password = "python123" 

print("==========================")

#                                     Encapsulation

# Private Variable

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)

account = BankAccount(5000)
account.deposit(2000)
account.withdraw(1000)
account.show_balance()
print("==========================")

# Encapsulation in Student   

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def result(self):
        if self.__marks >= 40:
            print("Pass")
        else:
            print("Fail")

student = Student(75)
student.result()
print("==========================")

# Private Password

class User:
    def __init__(self, password):
        self.__password = password

    def login(self, password):
        if password == self.__password:
            print("Login successful")
        else:
            print("Invalid password")

user = User("python123")
user.login("python123")
print("==========================")
