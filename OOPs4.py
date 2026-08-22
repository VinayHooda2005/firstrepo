# Multiple Inheritance

class Father:
    def skills(self):
        print("Driving")

class Mother:
    def talent(self):
        print("Cooking")

class Child(Father, Mother):
    pass

child = Child()
child.skills()
child.talent()
print("=================================")

# Hierarchical Inheritance

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meowing")

dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()
print("=================================")


# Hybrid Inheritance

class A:
    def show_a(self):
        print("A")

class B(A):
    def show_b(self):
        print("B")

class C(A):
    def show_c(self):
        print("C")

class D(B, C):
    def show_d(self):
        print("D")

obj = D()
obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()
print("=================================")

# Method Resolution Order

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.show()

print([cls.__name__ for cls in D.mro()])
print("=================================")

# object Class

class Student:
    pass

print(Student.__bases__)
print("=================================")

# __str__() Dunder Method

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

student = Student("Rahul")
print(student)
print("=================================")

# __len__() Dunder Method

class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

team = Team(["A", "B", "C"])
print(len(team))
print("=================================")

# __add__() and Operator Overloading

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(10)
b = Number(20)
print("=================================")

print(a + b)

# __eq__() Operator Overloading

class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

s1 = Student("Anushka")
s2 = Student("Anushka")

print(s1 == s2)
print("=================================")

# __lt__() and __gt__()

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

s1 = Student(90)
s2 = Student(75)

print(s1 > s2)
print("=================================")