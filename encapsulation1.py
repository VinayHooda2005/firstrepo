# Basic Encapsulation 

class Student:
    def __init__(self,marks):
        self.__marks=marks

    def show_marks(self):
        print("Marks =",self.__marks)

s1 = Student(90)
s1.show_marks()
print("============================")


class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:",self.__balance)

account = BankAccount(10000)
account.show_balance()
print("============================")


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary =salary

    def show_salary(self):
        print("Name =",self.name)
        print("Salary =",self.__salary)

employee = Employee('Vinay',30000)
employee.show_salary()
print("=================")


# Getter And Setter 

class Student:
    def __init__(self,marks):
        self.__marks=marks

    def get_marks(self):
        return self.__marks

student = Student(90)
print("Marks =",student.get_marks())
print("======================")


class Student:
    def __init__(self,marks):
        self.__marks=marks

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks=marks
        else:
            print("Invalid Marks")

student = Student(80)
print("Old Marks =",student.get_marks())

student.set_marks(90)
print("New Marks =",student.get_marks())
print("==========================")


class Student:
    def __init__(self,marks):
        self.__marks = marks

    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    def get_marks(self):
        return self.__marks

student = Student(80)
student.set_marks(150)

print("Marks =",student.get_marks())
print("==================")