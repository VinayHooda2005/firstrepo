class Person:
    def __init__(self,name,age=18):
        self.name=name
        self.age=age

    def greet(self):
        print("Hello",self.name)

p1=Person('Vinay',21)
p2=Person('Sawan')
p1.greet()

print(p2.age)

# Create an object
class Student:
    pass
s1=Student()
print("==================")

# Create multiple objects
class Car:
    pass

car1=Car()
car2=Car()
car3=Car()
print("==================")

# add an attribute
class Student:
    pass 
s1=Student()
s1.name='Rahul'
print(s1.name)
print("==================")

# Create two objects with different attributes
class Student:
    pass 
s1=Student()
s2=Student()
s1.name='Rahul'
s2.name='Vinay'
print(s1.name)
print(s2.name)
print("==================")

# students details

class Student:
    pass
s1=Student()
s1.name='Vinay'
s1.age='21'
s1.marks=90

print("Name=",s1.name)
print("Age=",s1.age)
print("Marks",s1.marks)
print("==================")

# create mobile class
class Mobile:
    pass

m1=Mobile()
m2=Mobile()

m1.brand="Samsung"
m2.brand="Apple"

print(m1.brand)
print(m2.brand)
print("==================")

# create a book class
class Book:
    pass

b1=Book()

b1.title="Python Programming"
b1.price=500

print("Title=",b1.title)
print("Price=",b1.price)
print("==================")

# add a method
class Student:
    def display(self):
        print("Welcome to python ")

s1=Student()
s1.display()
print("==================")

# real life class and object

class Employee:
    def display(self):
        print('Name=',self.name)
        print('Salary',self.salary)

e1=Employee()

e1.name='Rahul'
e1.salary=30000

e2=Employee()

e2.name='Anu'
e2.salary=25000

e1.display()
e2.display()