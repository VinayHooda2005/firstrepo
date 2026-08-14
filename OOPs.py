# A claas Student with attribute name,age. Display one object
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name=",self.name)
        print("Age=",self.age)

s1=Student('Vinay',21)
s1.display()
print("================================")

# A class Car with attribute brand, model. Display two object
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display(self):
        print("Brand=",self.brand)
        print("Model=",self.model)

c1=Car("Mahindra","Scorpio")
c2=Car("Toyoto","Fortuner")

c1.display()
c2.display()
print("===============================")  

# A class Rectangle with attributes length, width.Method area.Calculate area.
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width

r1=Rectangle(10,20)
print("Length=",r1.length)
print("Width=",r1.width)
print("Area of Rectangle=",r1.area())
print("==============================")

''' A parent class Animal with method sound.A child class Dog overrides sound.
   Create object of Dog class and 'call method '''
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Barks")

d1=Dog()
d1.sound()
print("==========================")

# A class Person have attribute name, age.Method Display.Call with two objects
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name=",self.name)
        print("Age=",self.age)

p1=Person('Rahul',22)
p2=Person('Priya',21)

p1.display()
p2.display()
print("=========================")

class BankAcount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Deposited=",amount)

    def withdraw(self,amount):
       if self.balance>=amount: 
         self.balance-=amount
         print("Withdraw=",amount)
       else:
           print("Insufficiant Balance")

    def display(self):
        print("Account_holder=",self.account_holder)
        print("Balance=",self.balance)

b1=BankAcount('Vinay',10000)

b1.display()
b1.deposit(5000)
b1.withdraw(8000)
b1.display()
print("====================")

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name=",self.name)
        print("Age=",self.age)

p1=Person('Rahul',22)
p2=Person('Priya',21)

p1.display()
p2.display()
print("=========================")

class BankAcount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Deposited=",amount)

    def withdraw(self,amount):
       if self.balance>=amount: 
         self.balance-=amount
         print("Withdraw=",amount)
       else:
           print("Insufficiant Balance")

    def display(self):
        print("Account_holder=",self.account_holder)
        print("Balance=",self.balance)

a=input("Enter account_holder=")
b=float(input("Enter balance="))

b1=BankAcount(a,b)

d=float(input("Deposited Amount="))
b1.deposit(d)

w=float(input("Withdraw Amount="))
b1.withdraw(w)

b1.display()



        