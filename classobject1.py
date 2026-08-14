class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def study(self):
        print("Hello",self.name)

s1=Student('Vinay',21)
print(s1.name)
s1.study()
print("===================")

class Stuident:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=Student("Rahul",20)
print(s1.name)
print("===============")

class Employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary

e1=Employee("Rahul",20,50000)
e2=Employee("Anu",19,45000)
print(e1.name,e1.emp_id,e1.salary)
print(e2.name,e2.emp_id,e2.salary) 
print("======================")

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length * self.breadth

r1=Rectangle(12,10)
print(r1.area())
print("================")

