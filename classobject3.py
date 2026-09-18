# Basic question of OOPs

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=Student('Vinay',21)
print(s1.name)
print(s1.age)
print("=======================")


class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

c1=Car('Mahindra','Scorpio',2500000)
c2=Car('Toyota','Fortuner',5000000)

print(c1.brand,c1.model,c1.price)
print(c2.brand,c2.model,c2.price)
print("==================")


class Person:
    def __init__(self,name,city):
        self.name=name
        self.city=city

p1=Person('Vinay','Rohtak')
print(p1.name)
print(p1.city)
print("=====================")


class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def display(self):
        print("Brand =",self.brand)
        print("Price =",self.price)

m1=Mobile('Samsung',30000)
m1.display()
print("==================")


class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department

e1=Employee('Vinay',30000,'IT')
e2=Employee('Jatin',35000,'Sales')
print(e1.name,e1.salary,e1.department)
print(e2.name,e2.salary,e2.department)
print("=======================")


# Methods in OOPs

class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        print("Sum =",self.a+self.b)

    def subtract(self):
        print("Difference =",self.a-self.b)

    def multiply(self):
        print('Multiplication =',self.a*self.b)

    def divide(self):
        print('Division =',self.a/self.b)


c1 = Calculator(20, 15)
c1.add()
c1.subtract()
c1.multiply()
c1.divide()

c2 = Calculator(54,27)
c2.divide()
c2.add()
print("==========================")


class BankAccont:
    def __init__(self,balance):
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Amount deposit =",amount)

    def withdraw(self,amount):
        if amount<=self.balance:
         self.balance-=amount
         print("Withdraw amount =",amount)
        else :
         print("Insufficiant balance")

    def check_balance(self):
        print("Current Balance =",self.balance)

account =BankAccont(10000)

account.check_balance()
account.deposit(5000)
account.check_balance()
account.withdraw(3000)
account.check_balance()
print("=======================")


class Student:
    def __init__(self,marks):
        self.marks=marks

    def result(self):
        if self.marks>=40:
            print("Pass")
        else:
            print("Fail")

s1 = Student(56)
s2 = Student(30)
s1.result()
s2.result()
print("==========================")


class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        a=self.l * self.b
        print("Area of Rectangle =",a)

    def perimeter(self):
        p=2*(self.l + self.b)
        print("Perimeter of Rectangle =",p)

r1 = Rectangle(10,20)
r1.area()
r1.perimeter()
print("=========================")


class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        a = 3.14 * self.radius * self.radius
        print("Area of circle =",a)

c1 = Circle(5)
c1.area()