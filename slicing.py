# print five character
s = "Programming"
print(s[:5])

#  extract three elements
nums = [10, 20, 30, 40, 50, 60]
print(nums[:3])

# reverse the string
s = "Python"
print(s[::-1])

# extract Artificial
text = "Artificial Intelligence"
print(text[:10])

#get last two color
colors = ["red", "blue", "green", "yellow", "black"]
print(colors[-2:])

#extract alternate
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[::2])

#extract second character
s = "DataScience"
print(s[::2])

# remove first and last element
marks = [45,67,89,90,34,56,78]
print(marks[1:-1])

#extract only learning
sentence = "Machine Learning with Python"
print(sentence[8:16])

# reverse middle four elements
nums = [100,200,300,400,500,600]
middle = nums[1:5][::-1]
result = [nums[0]] + middle + [nums[-1]]
print(result)

#extract the last two values from each  inner list
data = [[1,2,3],[4,5,6],[7,8,9]]
for row in data:
    print(row[-2:])

#extract characters from index 20 to index 5 in reverse
text = "abcdefghijklmnopqrstuvwxyz"
print(text[20:4:-1])

# replace middle four element
nums = [5,10,15,20,25,30,35,40]
nums[2:6] = [100,200,300,400]
print(nums)

# check palindrome or not
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# alternate elements in reverse order
data = [1,2,3,4,5,6,7,8,9,10]
new_list = data[::-2]