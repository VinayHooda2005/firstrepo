class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def final_price(self):
        return self.price

class Electronics(Product):
    def __init__(self, name, price,warranty):
        super().__init__(name, price)
        self.warranty=warranty

    def final_price(self):
        return self.price * 2

class Clothing(Product):
    def __init__(self, name, price,size):
        super().__init__(name, price)
        self.size=size

    def final_price(self):
        return self.price * 3

class Grocery(Product):
    def __init__(self, name, price,weight):
        super().__init__(name, price)
        self.weight=weight

    def final_price(self):
        return self.price * 1.5

products={
    Electronics("Laptop",50000,"2 Years"),
    Clothing("T-Shirt",1000,"XL"),
    Grocery("Rice",300,"5 Kg")
}

for product in products:
    print(product.name,product.final_price())

print("=============================")

#

class UniversityMember:
    def __init__(self,name):
        self.name=name

    def activity(self):
        pass

class Student(UniversityMember):
    def activity(self):
        print(self.name,"is attend class")

class Teacher(UniversityMember):
    def activity(self):
        print(self.name,"is teaching students")

class Researcher(UniversityMember):
    def activity(self):
        print(self.name,"is conducting research")

universitymembers={
    Student("Rahul"),
    Teacher("Dr. Sameer"),
    Researcher("Manoj")
}

for universitymember in universitymembers:
    universitymember.activity()

print("==========================")

#. Public Members

class Student:
    def __init__(self, name):
        self.name = name

student = Student("Vinay")
print(student.name)
print("==========================")

# Protected Members

class Student:
    def __init__(self):
        self._course = "Python"

class Child(Student):
    def show(self):
        print(self._course)

obj = Child()
obj.show()
print("==========================")

# Private Members
class Student:
    def __init__(self):
        self.__marks = 90

    def show_marks(self):
        print(self.__marks)

student = Student()
student.show_marks()
print("==========================")

# Name Mangling

def __init__(self):
    self.__marks = 90

student = Student()
print(student._Student__marks)
print("==========================")

# Class Variables

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Anu")
s2 = Student("Rahul")

print(s1.school)
print(s2.school)
print("==========================")

# Instance Variables

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Anu", 23)
s2 = Student("Rahul", 22)

print(s1.name, s1.age)
print(s2.name, s2.age)
print("==========================")

# super()

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

dog = Dog()
dog.sound()
print("==========================")

# super() with Constructor

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

student = Student("Vinay", "Python")

print(student.name)
print(student.course)
print("==========================")

# Single Inheritance

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

dog = Dog()
dog.eat()
dog.bark()
print("==========================")

# Multilevel Inheritance

class Animal:
    def eat(self):
        print("Eating")

class Mammal(Animal):
    def walk(self):
        print("Walking")

class Dog(Mammal):
    def bark(self):
        print("Barking")

dog = Dog()
dog.eat()
dog.walk()
dog.bark()
print("==========================")