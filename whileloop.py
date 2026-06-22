# while loop that print numbers from 1 to 10
print("Numbers from 1 to 10:")
i = 1
while i <= 10:
    print(i)
    i += 1


# while loop that prints even numbers from 1 to 20
print("Even numbers from 1 to 20:") 
i = 2
while i <= 20:
    print(i)
    i += 2


# while loop that calculates the sum of numbers from 1 to 100
print("Sum of numbers from 1 to 100:")
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print(total)


# while loop that prints the multiplication table of 7
print("Multiplication table of 7:")
i = 1
while i <= 10:
    print("7*", i, "=", 7*i)
    i += 1


# while loop to reverse the number 1234
print("Reverse of the number 1234 :")
num=1234
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print(reverse)


# while loop to find the factorial of a number
print("Factorial of 5:")
i = 5
factorial = 1
while i >= 1:
    factorial =factorial * i
    i = i - 1
print(factorial)


#while loop to check if a number is prime or not
print("Check if a number is prime or not:")
num = 29
is_prime = True
i = 2
while i < num:
    if num % i == 0:
        is_prime = False
        break
    i += 1
if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")


# while loop to count the number of 1234
print("Count of digits in 1234:")
num = 1234
count = 0
while num > 0:
    num = num // 10
    count =count + 1
print(count)


# while loop for Fibonacci series up to 100
print("Fibonacci series up to 100:")        
a, b = 0, 1
while a <= 100:
    print(a, end=" ")
    a, b = b, a + b


# While loop that keep asking the user to enter password until the correct password is entered
print("\nEnter the password (Hint: it's 'python'):")
password = ""
correct_password = "python"

while password != correct_password:
    password = input("Password: ")
print("Access granted!")