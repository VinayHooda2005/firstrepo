# number print from 1 to 100

#in while loop
n=1
print("number from 1 to 100")
while n<=100:
    print(n)
    n=n+1

# in for loop
for i in range(1,101):
    print(i)
print("=====================")


# even number between 1 to 100

# in while loop
i=2
print("Even number between 1 to 100")
while i<=100:
    print(i)
    i=i+2

# in for loop
for i in range(2,101,2):
    print(i)
print("===================")


# sum of odd number between 1 to 100

# in while loop
i=1
sum=0
print("sum of odd number between 1 to 100")
while i<100:
    print(i)
    sum=sum+i
    i=i+2
print("Sum =",sum)

# in for loop
sum=0
for i in range(1,100,2):
    sum=sum+i
print("Sum =",sum)
print("==============")


# multiplication table of number
n=int(input("Enter a number="))
print(f"Multiplication table of {n}")
i=1
while i<=10:
    print(f"{n}*{i} =",n*i)
    i=i+1
print("=================")


# factorial of a number 
num=int(input("Enter a number ="))
print(f"Factorial of {num} =",end=" ")
factorial=1
while num>0:
      factorial=factorial*num
      num=num-1
print(factorial)


# number ke digit ka sum
num=int(input("Enter a number ="))
print(f"sum of digits of number {num} is = ",end=" ")
sum=0
while num>0:
    digit= num % 10
    sum=sum+digit
    num =num // 10
print(sum)
print("=================")



# number reverse
num=int(input("Enter a number ="))
print(f"Reverse of number {num} is = ",end=" ")
reverse=0
while num>0:
    digit= num % 10
    reverse=reverse*10+digit
    num =num // 10
print(reverse)
print("=================")


# check armstrong number
number=int(input("Enter a number ="))
temp=number
n=len(str(number))
armstrong_sum=0
while number>0:
    digit=number%10
    armstrong_sum=armstrong_sum+digit ** n
    number=number//10
if armstrong_sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")
print("====================")


# check palindrome 
number=int(input("Enter a number ="))
temp=number
reverse = 0
while number > 0:
    digit = number%10
    reverse = reverse*10 + digit
    number = number//10
if reverse == temp:
    print("Palindrome")
else:
    print("Not Palindrome")
print("===================")


# fibonacci series
a=0
b=1
while a<7:
    print(a,end=" ")
    a,b=b,a+b
