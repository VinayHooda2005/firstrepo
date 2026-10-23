# Student class

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name = {self.name} Age = {self.age}")

s1 = Student("Vinay Hooda","21")
s1.display()
print("============================")

# Car class

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def show(self):
        print("Brand =",self.brand)
        print("Model =",self.model)

c1 = Car("Mahindra","Scorpio") 
c1.show()
print("============================")


# Inheritance 

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print("Animal make sound")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")

dog1 = Dog("Tommy")
dog1.bark()

dog1.sound()