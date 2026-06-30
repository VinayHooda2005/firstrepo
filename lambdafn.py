# lamda parameter:expression
add=lambda a,b:a+b
print(add(2,3))

# Question 1:
x=12               #global variable

def divide(a):
    b=10           #local variable
    div=a//b
    return div
print(divide(30))

print(x)

#Question 2:
name="Rahul"

def Name():
    print(name)
Name()

# Question 3:
x=10
def show():
    x=20
    print(x)
show()
print(x)

#Question 4:
square=lambda a:a*a
print(square(2))


#Question 6:
cube=lambda b:b*b*b
print(cube(2))

#Question 7:
mul=lambda a,b:a*b
print(mul(3))
