# to find even or odd
def is_even_odd(number):
    if number%2==0:
        print("Even")
    else:
        print("Odd")

is_even_odd(45)
print("=================")


# factorial ka function
def factorial(n):
    fact=1
    while n>0:
        fact=fact*n
        n=n-1
    return fact

print(factorial(5))

def Factorial(x):
    if x<0:
        return "input error(negative input)"
    factor = 1
    for i in range(1,x+1):
        factor=factor*i
    return factor

print(Factorial(5))
print("=================")


# check prime or not
def prime(n):
    if n<=1:
        return "invalid input enter a number upto 1"

    for i in range(2,int(n**0.5)+1):
      if  n%i==0:
            return "Not Prime"
    return "Prime"

print(prime(36))
print(prime(2))
print("===================")


# find  largest in a list
def find_largest(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst:
        if num>largest:
            largest=num
    return largest
print(find_largest([2,4,78,43,81]))
print("=================")


# find average of multiple numbers
def calcu_average(numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)

print(calcu_average((10,20,30,40,50)))
print("==================")


# *args use for sum
def sum_all(*args):
    return sum(args)

print(sum_all(10,30,40))
print("==================")


# Recursive factorial 
def factorial_recursive(n):
    if n<0:
        return "Invalid Input"
    if n==0 or n==1:
        return 1
    return n*factorial_recursive(n-1)

print(factorial_recursive(5))
print("=================")


# Recursive Fibonacci function
def fibonacci_recursion(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
print(fibonacci_recursion(4))
print("===================")


# return second largest in a list
def second_largest(lst):
    unique_number=list(set(lst))
    if len(unique_number)<2:
        return None
    unique_number.sort()
    return unique_number[-2]
print(second_largest((23,43,32,57,17)))
print("===============")


# use **kwargs for display details
def user_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
user_details(name="Vinay",age=21)