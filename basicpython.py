# To store a name in variable
name = "Vinay Hooda"
print(name)
print("==========================")

# To find datatype
age = 22
name = "Vinay Hooda"

print(type(age))
print(type(name))
print("==========================")


# Input from user and sum of two numbers
num1 = int(input("Enter first number ="))
num2 = int(input("Enter second number ="))

sum = num1 + num2
print("Sum of two number =",sum)
print("==========================")


# To calculate area of circle
radius = 12
pi = 3.14

area = pi * radius * radius
print("Area of circle =", area)
print("====================")


# To find number is even or odd
num = int(input("Enter a number ="))
if num % 2 == 0 :
    print(f"{num} is even number")
else :
    print(f"{num} is odd number")
print("==========================")


# To check pass or fail 
marks = int(input("Enter marks ="))
if marks >= 33 :
    print("Pass")
else :
    print("Fail")
print("==========================")


# Age check program
age = int(input("Enter your age ="))
if age >= 18 :
    print("Eligible")
else :
    print("Not eligible")
print("==========================")


# to find largest of three

a = int(input("Enter a ="))
b = int(input("Enter b ="))
c = int(input("Enter c ="))
if a >= b and a >= c:
    print(f"{a} is greater")
elif b >= a and b >= c:
    print(f"{b} is greater")
else :
    print(f"{c} is greater")
print("==========================")


# to print 1 to 10 in for loop

for i in range (1,11):
    print(i)
print("==========================")


# To print even from 1 to 100 in loop 

print("Even from 1 to 100 are =")
for i in range(2,101,2):
    print(i)


# Table program

num = int(input("Enter a number ="))
for i in range(1,11):
    print(num * i)
print("==========================")


# To find factorial

num = int(input("Enter a factorial number ="))
fact = 1
while num >= 1 :
    fact *= num
    num = num-1
print("Factorial = ",fact)
print("==========================")


# Reverse counting
num = 10
while num >= 1:
    print(num)
    num -= 1
print("==========================")


# String reverse

str = "python"
print("Reversed =",str[::-1])
print("==========================")


# check palindrome or not 
str = input("Enter a string =")
if str == str[::-1] :
    print("Palindrome ")
else :
    print("Not palindrome")
print("==========================")


# Vowel count
str = input("Enter a string =")
vowels = "aeiouAEIOU"
count = 0

for char in str:
    if char in vowels:
        count += 1
print("Number of vowels =",count)
