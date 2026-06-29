# # Question 1:input name,age and greeting

# name=input("Name=")
# age=int(input("Age="))
# print("Welcome",name)
# print("Age=",age)

# #Question 2:find sum,difference,product,division

# a=float(input("Enter First Number="))
# b=float(input("Enter Second Number="))
# print("sum=",a+b)
# print("difference=",a-b)
# print("product=",a*b)
# print("division=",a//b)

# #Question 3 swap two number with third variable
# num1=int(input("Enter num1="))
# num2=int(input("Enter num2="))
# print("number before swap are","num1=",num1,"num2=",num2)
# temp=num1
# num1=num2
# num2=temp
# print("number after swap are","num1=",num1,"num2=",num2)

# #Question 4:convert celsius to fahrenheit
# num=float(input("celsius="))
# fahrenheit=(1.8*num)+32
# print(fahrenheit)

# #Question 5:area of circle
# pi=3.14
# radius=int(input("enter radius="))
# area=pi*radius*radius
# print("area of circle=",area)


# #operator&condition

# #Question 6:check even or odd
# num=int(input("enter number="))
# if num%2==0:
#     print("Even")
# else:
#     print("Odd")


# # Question 7:largest among three
# a=int(input("Enter First Number="))
# b=int(input("Enter Second Number="))
# c=int(input("Enter Third Number="))

# if a>=b and a>=c:
#     print("Large=",a)
# elif b>=a and b>=c:
#     print("Large=",b)
# else :
#     print("Large=",c)


# # Question 8:check leap year
# year=int(input("enter year="))
# if year%4==0:
#     print("year is leap")
# else:
#     print("year is not leap")


# #Queston 9:print grade
# marks=int(input("Enter Marks="))
# if marks>=90:
#     print("grade A")                   #20,21,24,25
# elif marks>=80:
#     print("grade B")
# elif marks>=70:
#     print("grade C")
# else:
#     print("grade D")


# #Question 10:simple calculator
# num1=float(input("enter num1="))
# num2=float(input("enter num2="))
# operator=(input("enter operator(+,-,*,/):="))

# if operator=="+":
#     result=num1+num2
#     print("Result=",result)
# elif operator=="-":
#     result=num1-num2
#     print("Result=",result)
# elif operator=="*":
#     result=num1*num2
#     print("Result=",result)
# elif operator=="/":
#     if num2 !=0:
#         result=num1/num2
#         print("Result=",result)
#     else :
#         print("error:division by zero")
# else:
#     print("invalid operator")

# #loops

# # Question 11:print 1 to 100
# i=1
# print("number from 1 to 100=")
# while i<=100:
#     print(i)
#     i=i+1


# # Question 12:multplication table

# i=1
# while i<=10:
#     print("7*",i,"=",7*i)
#     i=i+1


# # Question 13:sum of first N number

# i=1
# sum=0

# while i<=10:
#     sum=sum+i
#     i=i+1
# print("sum=",sum)


# # Question 14:factorial

# i=int(input("enter a number="))
# factorial=1
# while i>=1:
#     factorial=factorial*i
#     i=i-1
# print("factorial of 5=",factorial)


# #Question 15:count even odd 1 to n
# num=1
# even=0
# odd=0
# while num<=10:
#     if num%2==0:
#         even=even+1
#     else:
#         odd=odd+1
#     num=num+1
# print("count even=",even)
# print("count odd=",odd)


# # Question 16:reverse of number
# num=int(input("Enter number="))
# reverse=0
# while num>0:
#         digit=num%10
#         reverse=reverse*10+digit
#         num=num//10
        
# print("Reverse of num=",reverse)

# #Question:17 check armstrong number
number=153
n=len(str(number))
armstrong_sum = 0
while number> 0:
       digit = number% 10
       armstrong_sum += digit ** n
       number //= 10
if armstrong_sum == number:
    print("armstrong")
else:
    print("not armstrong"),


# #Strings

# #Question 18:count vowels and consonants
# str=input("Enter a text=")
# vowels_count=0
# consonants_count=0
# space_count=0
# vowels="aeiouAEIOU"

# for char in str:
#     if char in vowels:
#         vowels_count+=1
#     elif char ==" ":
#         space_count+=1
#     elif char.isalpha:
#         consonants_count+=1
# print("vowel counts are=",vowels_count)
# print("space counts are=",space_count)
# print("consonants count are=",consonants_count)

# # Question 19: check palindrome
# num = input("Enter number=")
# if num == num[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# # Question 22:count words in a sentence

# sentence=input("Enter a word=")
# word=sentence.split()
# print(len(word))


# #Question 23:prime or not

# num=int(input("Enter a number="))
# is_prime=True
# i=2
# while i<num:
#     if num%i==0:
#         is_prime=False
#         break
#     i=i+1
# if num<=1:
#     is_prime=False
# if is_prime:
#     print(num,"is a prime number")
# else:
#     print(num,"is not a prime")











