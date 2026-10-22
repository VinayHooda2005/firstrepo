# Add items in list
fruits = ["Apple","Banana"]


# Largest element in list
nums = [10,34,23,54]
print(max(nums))
print("========================")


# List sum
nums = [10,34,23,54]
print(sum(nums))
print("========================")


# Duplicate remove
nums = [ 23,56,49,56,78]
print(list(set(nums)))

nums = [ 23,56,49,56,78]
print(list(dict.fromkeys(nums)))
print("========================")


# Dictionary 

student = {
    "name":"Vinay Hooda",
    "age":22
}

# Add new key
student["city"]="Rohtak"
print(student)
print("========================")


# Add function 
def add(a,b):
    sum = a + b
    print("Sum =",sum)
add(10,20)

def add(a,b):
    return a + b

print("Sum =",add(10,20))
print("======================")


# Prime number function

def is_prime(num):
    if num <= 1 :
        print(f"{num} is not a prime number")
        return
    
    for i in range(2,int(num ** 0.5) +1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            return
    
    print(f"{num} is a prime number")

is_prime(17)
is_prime(22)
