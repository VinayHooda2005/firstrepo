#giving s="Programming" 
s = "Programming"
print(s[:5])


nums = [10, 20, 30, 40, 50, 60]
print(nums[:3])


s = "Python"
print(s[::-1])

text = "Artificial Intelligence"
print(text[:10])

colors = ["red", "blue", "green", "yellow", "black"]
print(colors[-2:])

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[::2])

s = "DataScience"
print(s[::2])

marks = [45,67,89,90,34,56,78]
print(marks[1:-1])

sentence = "Machine Learning with Python"
print(sentence[8:16])



nums = [100,200,300,400,500,600]
middle = nums[1:5][::-1]
result = [nums[0]] + middle + [nums[-1]]
print(result)


data = [[1,2,3],[4,5,6],[7,8,9]]
for row in data:
    print(row[-2:])


text = "abcdefghijklmnopqrstuvwxyz"
print(text[20:4:-1])


nums = [5,10,15,20,25,30,35,40]
nums[2:6] = [100,200,300,400]
print(nums)
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


data = [1,2,3,4,5,6,7,8,9,10]
new_list = data[::-2]