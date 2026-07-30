import numpy as np
arr=np.array([[2,3,8,5],[0,-1,6,-2],[3,4,8,5]])
arr2=arr[:2,::2]
print(arr2)

arr3=arr[[1,1,0],[3,2,1]]
print(arr3)

arr4=np.array((2,5,3))
print(arr4)

arr5=np.array([3,8,4])
print(arr5)

print("=============")
print("=============")
#Question 1
print("Welcome to Python Programming")
print("=============")

#Question 2
name="Vinay Hooda"
age=21
city="Rohtak"
print("Name=",name)
print("Age=",age)
print("City=",city)
print("=============")

#Question 3
name=input("Enter Your Name=")
age=input("Enter Your Age=")
print("Name=",name)
print("Age=",age)
print("=============")

#Question 4
num1=float(input("Enter num1="))
num2=float(input("Enter num2="))
print("Addtion=",num1+num2)
print("Substraction=",num1-num2)
print("Multiplication=",num1*num2)
print("Division=",num1/num2)
print("=============")

#Question 5
l=int(input("Enter length="))
b=int(input("Enter breadth="))
area=l*b
print("Area of rectangle=",area)
print("=============")

#Question 6
numbers=[10,20,30,40,50]
print(numbers[::2])
print("=============")

#Question 7
names=['Vinay','Jatin','Sawan']
print(names)
print("=============")

#Question 8
fruits=['Apple','Banana','Mango']
fruits.append('Orange')
print(fruits)
print("=============")

#Question 9
numbers=[10,20,30,40,50]
numbers.remove(30)
print(numbers)
print("=============")

#Question 10
numbers=[10,20,30,40,50]
print(len(numbers))
print("=============")


import numpy as np
#Question 11
import numpy as np
print("NumPy Imported Successfully")
print("=============")

#Question 12
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr)
print("=============")

#Question 13
import numpy as np
arr=np.array([1,2,3,4,5])
print(type(arr))
print("=============")

#Question 14
import numpy as np
marks=np.array([75,80,65,90,85])
print(marks)
print("=============")

#Question 15,16
arr=np.array([10,20,30,40,50])
print(arr[0])
print("=============")
print(arr[2])
print("=============")

#Question 17
arr=np.array([5,10,15,20,25])
print(arr[-1])
print("=============")

#Question 18,19
arr=np.array([10,20,30,40,50])
print(arr[:3])
print("=============")
print(arr[1:4])
print("=============")

#Question 20
arr=np.array([5,10,15,20,25,30])
arr[2]=100
print(arr)
print("=============")

#Question 21,22,23
arr=np.array([10,20,30,40,50])
print(arr.ndim)
print("=============")
print(arr.shape)
print("=============")
print(arr.size)
print("=============")

#Question 24
arr=np.array([10,20,30])
print(arr.dtype)
print("=============")

#Question 25
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print("=============")






