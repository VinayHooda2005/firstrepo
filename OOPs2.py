# Employee Management = Different employees perform different types of work

class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer is writing a code" )

class Designer(Employee):
    def work(self):
        print("Designer is creating design")

class Manager(Employee):
    def work(self):
        print("Manager is managing the team")

employees ={
    Developer(),
    Designer(),
    Manager()
}

for employee in employees:
    employee.work()
print("============================")

# Payment System = Different payment methods process payment in different ways

class Payment:
    def __init__(self,amount):
        self.amount=amount

    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print(f"Pay Rs {self.amount} through UPI")

class CreditCard(Payment):
    def pay(self):
        print(f"Pay Rs {self.amount} through CreditCard")

class NetBanking(Payment):
    def pay(self):
        print(f"Pay Rs {self.amount} through NetBanking")

payments={
        UPI(150),
        CreditCard(200),
        NetBanking(180)
        }

for payment in payments:
    payment.pay()

print("==================")

# School Management = Students and teacher display their details differently

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name =",self.name,"Age =",self.age)

class Student(Person):
    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no=roll_no

    def display(self):
        print("Student =",self.name,"Age =",self.age,"Roll No =",self.roll_no)

class Teacher(Person):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject=subject

    def display(self):
        print("Teacher =",self.name,"Age =",self.age,"Subject =",self.subject)

persons={
    Student("Rahul",21,101),
    Teacher("Anu",26,"Python"),
    Student("Aman",22,102),
    Teacher("Ravi",28,"SQL")
}

for person in persons:
    person.display()

print("=======================")

# Shape Area System = Different shapes calculate their area using own methods

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius *self.radius

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self,base,hight):
        self.base=base
        self.hight=hight

    def area(self):
        return 0.5 * self.base * self.hight

shapes={
    Circle(5),
    Rectangle(10,20),
    Triangle(5,10)
}

for shape in shapes:
    print(shape.area())
print("========================")

# Banking System = Savings and current account follows different deposit and withdral rules

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Savings: Withdrawn ₹{amount}")
        else:
            print("Savings: Insufficient balance")


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance + 5000:
            self.balance -= amount
            print(f"Current: Withdrawn ₹{amount}")
        else:
            print("Current: Withdrawal limit exceeded")


accounts = [
    SavingsAccount(10000),
    CurrentAccount(10000)
]

for account in accounts:
    account.deposit(2000)
    account.withdraw(12000)
    print("Balance:", account.balance)
