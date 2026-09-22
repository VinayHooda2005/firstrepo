# Real-world Example of Encapsulation in Python


# Bank Account

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("Deposit successful")
        else:
            print("Invalid deposit")

    def withdraw(self,amount):
        if amount>self.__balance:
            print("Insufficient balance")
        elif amount<=0:
            print("Invalid withdrawl")
        else:
            self.__balance-=amount
            print("Withdrawl successful")

    def get_balance(self):
        return self.__balance

account = BankAccount(10000)
print("Balance =",account.get_balance())
account.deposit(2000)
print("Balance =",account.get_balance())
account.withdraw(5000)
print("Balance =",account.get_balance())
print("========================")


# ATM PIN

class ATM:
    def __init__(self,pin):
        self.__pin = pin

    def check_pin(self,entered_pin):
        if entered_pin == self.__pin:
            print("Correct PIN")
        else:
            print("Incorrect PIN")

atm = ATM(1234)

atm.check_pin(3456)
atm.check_pin(47822)
atm.check_pin(1234)
print("========================")


# Mobile Phone

class Mobile():
    def __init__(self,battery):
        self.__battery = battery

    def charge(self,amount):
        self.__battery += amount

        if self.__battery > 100:
            self.__battery = 100

    def show_battery(self):
        print("Battery =",self.__battery,"%")

mobile = Mobile(60)

mobile.charge(30)
mobile.show_battery()

mobile.charge(50)
mobile.show_battery()