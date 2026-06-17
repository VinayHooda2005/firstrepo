# num check
num=int(input("enter num="))

if num%2==0:
    print("even number")
else:
    print("odd number")




#  positive negative or zero
number=int(input("enter number="))
if number<0:
    print("negative number")
elif number==0:
    print("mumber is zero")
else :
    print("positive number")




#largest two number
a=int(input("enter value a="))
b=int(input("enter value b="))

#print("largest number is :", max(a,b))
  

if a>=b:
    print("a is large")
else:
    print("b is large")

#largest three number
a=int(input("enter value a="))
b=int(input("enter value b="))
c=int(input("enter value c="))

#print("largest number is :", max(a,b,c))

if a>=b and a>=c :
    print("value a is largest")
elif b>=a and  b>=c:
   print("value b is large")
else:
    print("value c is large")


#to find grade
marks=int(input("enter your marks="))

if marks>=90:
    print("grade a")
elif marks>=80:
    print("grade b")
elif marks>=70:
    print("grade c")
else:
    print("grade e")



# is eligible for vote or not
age=int(input("enter your age ="))

if age>=18:
    print("eligible fo vote")
else:
    print("not eligible for vote")


# proram fo leap year 
year=int(input("enter year="))

if year%4==0:
    print("year is leap")
else :
    print("year is not leap")
