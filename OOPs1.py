'''A class Vehicle with method start().Two child class Car and Bike that
override start()with different message. Call method with child class object '''

class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting")

car=Car()
bike=Bike()

car.start()
bike.start()
print("=========================")

'''A class Student with Attribute name, marks.Use method to calculate_grade()
    and a  method display().Call it with three objects'''

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def calculate_grade(self):
        if self.marks >=90:
            return "A"
        elif self.marks >=80:
            return "B"
        elif self.marks >=70:
            return "C"
        elif self.marks >=60:
            return "D"
        elif self.marks >=50:
            return "E"
        else:
            return "F"

    def display(self):
        print("Name =",self.name)
        print("Marks =",self.marks)
        print("Grade =",self.calculate_grade())

s1=Student("Rahul",84)
s2=Student("Anu",90)
s3=Student("Priya",34)

s1.display()
s2.display()
s3.display()
print("=============================")

'''A parent class Shape with method area(). Child classes Circle and Rectangle that override 
   area().Store both object in a list and call area() for each object using loop '''

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width

shapes={
    Circle(5),
    Rectangle(10,20)
}

for shape in shapes:
    print("Area :",shape.area())
print("==========================")

'''A class Product with attributes name, price ,quantity. Add method total_price() to calculate 
   price * quantity.Create three objects and display their total prices. '''

class Product:
    def __init__(self,name,price,quantity): 
        self.name=name
        self.price=price
        self.quantity=quantity

    def total_price(self):
        return self.price * self.quantity


p1=Product("Pen",20,10)
p2=Product("Pencil",10,5)
p3=Product("eraser",5,10)

print("Name =",p1.name,"Total_Price =",p1.total_price())
print("Name =",p2.name,"Total_Price =",p2.total_price())
print("Name =",p3.name,"Total_Price =",p3.total_price())
print("============================")

''' A class Animal with attribute name. Create child classes Dog and Cat.
    Each class have its own sound() method. Using a loop call method sound()'''

class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print(self.name,"says Bark")

class Cat(Animal):
    def sound(self):
        print(self.name,"says Meow")

animals={
    Dog("Tommy"),
    Cat("Kitty")
}

for animal in animals:
    animal.sound()
print("===========================")

'''A class Employee with attribute name, salary.A child class Developer that adds a programming_language
    attribute.Create two developer objects and display all information'''

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Developer(Employee):
    def __init__(self, name, salary,programming_language):
        super().__init__(name, salary)
        self.programming_language=programming_language

    def display(self):
        print("Name =",self.name)
        print("Salary =",self.salary)
        print("Language =",self.programming_language)

d1=Developer("Rahul",60000,"Python")
d2=Developer("Anu",55000,"Java")

d1.display()
d2.display()
print("======================")

''' A class Person with method introduce(). Create child classes Student and teachers that override 
    introduce() differently.Create object of both classes and demonstrate polymorphism .'''

class Parent:
    def introduce(self):
        print("I am a person")

class Student(Parent):
    def introduce(self):
        print("I am a student")

class Teacher(Parent):
    def introduce(self):
        print("I am a teacher")

student=Student()
teacher=Teacher()

student.introduce()
teacher.introduce()
print("=====================")

'''Create a class Book with a contructor for title,author,and price.Add a method display(). Create a child class
   EBook that adds file_size .Use inheritance and constructors to display complete EBook information.'''

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def display(self):
        print("Title =",self.title)
        print("Author =",self.author)
        print("Price =",self.price)

class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size=file_size

    def display(self):
        print("Title =",self.title)
        print("Author =",self.author)
        print("Price =",self.price)
        print("File Size =",self.file_size)

e1=EBook("Python Basic","John",500,300)

e1.display()
