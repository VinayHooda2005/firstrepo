# Advanced 

# Employee Salary Validation

class Employee:
    def __init__(self,salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if salary >= 0:
            self.__salary = salary
            print("Salary Updated")
        else :
            print("Salary cannot be negative")

employee = Employee(30000)
print(employee.get_salary())

employee.set_salary(45000)
print(employee.get_salary())

employee.set_salary(-5000)
print("==================")


# Product Price

class Product:
    def __init__(self,name,price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self,price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be greater than 0")

product = Product("Laptop",50000)
print("Price =",product.get_price())

product.set_price(55000)
print("New Price =",product.get_price())

product.set_price(-10000)
print("================")


# Password Protection

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def login(self, password):
        if password == self.__password:
            print("Login Successful")
        else:
            print("Wrong Password")


user = User("vinay", "abc123")

user.login("abc123")
user.login("wrong123")