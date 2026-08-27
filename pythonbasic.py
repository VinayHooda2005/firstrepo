print("greet youself")
name=input("Enter your name =")
print("Hello ",name)
print("================")


print("add,subtract,multiply,divide of two number")
num1=float(input("Enter First number ="))
num2=float(input("Enter Second number ="))

print("Sum =",num1 + num2)
print("Subtraction =",num1-num2)
print("Multiplication =",num1*num2)
print("Division =",num1/num2)
print("=================")


print("check number is even or odd")
num=int(input("Enter a number ="))
if num % 2 == 0 :
    print("Even number")
else:
    print("Odd number")
print("================")


print("Check number is positive,negative,zero")
num=int(input("Enter a number ="))
if num>0:
    print("number is positive")
elif num==0:
    print("zero")
else:
    print("number is negative")
print("==================")


print("find large among three number")
a=int(input("Enter a ="))
b=int(input("Enter b ="))
c=int(input("Enter c ="))
print("Large number is =",max(a,b,c))
print("==============")

print("Check number is divisible by 5 and 11")
num=int(input("Enter a number ="))
if num % 5 == 0 and num % 11 == 0:
    print("number is divisible by 5 and 11")
else:
    print("number is not divisible 5 and 11")
print("==================")


print("find grade according to marks")
marks=float(input("Enter marks ="))
if marks>=90 and marks<100:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
elif marks>=60:
    print("Grade D")

else:
    print("Fail")
print("=================")


print("convert celsius to fahrenheit")
celsius =float(input("Celsius ="))
fahrenheit=(celsius * 9/5) + 32
print(f"{celsius}°c={fahrenheit}°f")
print("===============")

print("calculate simple interest")
p=int(input("Enter Principal amount ="))
r=int(input("Enter Rate of interest(%) ="))
t=int(input("Enter Time(in years) ="))
si=(p*r*t)/100
print("Simple Interest =",si)
print("=================")


print("swap two number")
a=int(input("Enter value of a ="))
b=int(input("Enter value of b ="))
print(f"before swap a={a}, b={b}")
a,b=b,a
print(f"after swap a={a}, b={b}")