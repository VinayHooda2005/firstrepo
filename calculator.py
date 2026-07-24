
def calculator(num1, num2, operator):

    if operator=="+":
        result=num1+num2
        print("sum=",result)
    elif operator=="-":
        result=num1-num2
        print("Difference=",result)
    elif operator=="*":
        result=num1*num2
        print("Product=",result)
    elif operator=="/":
        result=num1/num2
        print("Division=",result)
    elif operator=="//":
        result=num1//num2
        print("Floor Division=",result)
    elif operator=="%":
        result=num1%num2
        print("modules=",result)
    else:
        print("Please enter operator")


calculator(10, 20, "+")
calculator(20,15,"-")



# def add(a,b):
#     return a+b
# print(add(10,20))
# def sub(a,b):
#     return a-b
# print(sub(20,10))
# def mul(a,b):
#     return a*b
# print(mul(10,20))
# def div(a,b):
#     return a/b
# print(div(20,10))     






a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# def add(a, b):
#     return a + b
# print(add(a, b))