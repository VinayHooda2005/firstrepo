#Question 10
n=5
if n%2==0:
    print("even",n)
else:
    print("not even",n)

#question 11
l=int(input("enter length="))
b=int(input("enter breadth="))
area=l*b
perimeter=2*(l+b)
print("area of rectangle=",area)
print("perimeter of rectangle=",perimeter)


#question 12
num=int(input("enter number="))
if num<0:
    print("negative number")
elif num==0:
    print("zero")
else :
    print("positive")

#question 13
i=0
print("even number between 1 to 50 are=")
while i<50:
    i=i+2
    print(i)

#question 14
num=int(input("enter num="))
i=2
while i<num:
    if num%i==0:
        print("not prime")
        exit()
    i=i+1
print("prime")

# question 15
try:
    a=int(input("enter first number="))
    b=int(input("enter second number="))
    division=a/b
    print(division)
except ZeroDivisionError:
    print("enter valid number")


#question 16
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

num=2
while num<=50:
    print(num)
    num=num+2


def is_prime(n):
    if n<=1:
        return False
    for i in range (2,int(n%2==0)+1):
        if n%i==0:
            return False
        return True
print(is_prime(7))