# Multilevel Inheritance in OOPs

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Puppy(Dog):
    def play(self):
        print("Puppy is playing")

puppy =Puppy()

puppy.eat()
puppy.bark()
puppy.play()
print("===================")


class Person:
    def __init__(self,name):
        self.name=name

class Employee(Person):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary=salary

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name,salary)
        self.department=department

manager = Manager("Vinay",30000,"IT")
print("Name =",manager.name)
print("Salary =",manager.salary)
print("Department =",manager.department)
print("===========================")


class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class SportsCar(Car):
    def turbo(self):
        print("Sports car is using turbo")

sc = SportsCar()
sc.start()
sc.drive()
sc.turbo()
print("============================")


# Multiple Inheritance in OOPs

class Father:
    def father_property(self):
        print("Child has father's house")

class Mother:
    def mother_property(self):
        print("Child has mother jewelry")

class  Child(Father,Mother):
    pass

c1 = Child()
c1.father_property()
c1.mother_property()
print("======================")


class Phone:
    def make_calls(self):
        print("Calling...")

class Camera:
    def take_photo(self):
        print("Photo taken")

class SmartPhone(Phone,Camera):
    pass

sp = SmartPhone()
sp.make_calls()
sp.take_photo()
print("====================")


