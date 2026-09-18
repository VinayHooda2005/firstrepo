# Single Inheritance

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    pass

d1 = Dog()
d1.eat()
print("==========================")\


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self, name, age,course):
        super().__init__(name,age)
        self.course=course

    def display(self):
        print("Name =",self.name)
        print("Age =",self.age)
        print("Course =",self.course)

s1 = Student("Vinay",21,"Python")
s1.display()
print("=======================")


class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
        pass

c1 = Car()
c1.start()
print("===================")

# Constructor + Inheritance

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class Car(Vehicle):
    def __init__(self, brand, model,price):
        super().__init__(brand,model)
        self.price=price

c1 = Car('Mahindra','Scorpio',2000000)
print("Brand =",c1.brand)
print("Model =",c1.model)
print("Price =",c1.price)
print("==================================")


# Method Overriding

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog makes sound")

d1 = Dog()
d1.sound()
print("=====================")


class Employee:
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def work(self):
        print("Manager is managing the team")

m1 = Manager()
m1.work()
print("==================")