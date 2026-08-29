# largest and smallest 

lst=[22,45,31,25,13]
smallest=min(lst)
largest=max(lst)
print(lst)
print("Smallest =",smallest)
print("Largest =",largest)
print("===============")


# second largest
lst=[22,45,31,25,13]
lst.sort()
print("Second Largest =",lst[-2])
print("=================")


# remove duplicate
lst=[1,2,2,3,4,5,5,6,7]
unique_list=list(dict.fromkeys(lst))
print("Unique List =",unique_list)
print("===================")


# reverse list without reverse()
lst=[1,2,4,5,7,8]
print(lst[::-1])
print("===============")


# even or odd in a list
lst=[1,2,3,4,5,6,7,8,9]
evens = [x for x in lst if x%2 ==0 ]
odds = [x for x in lst if x%2 !=0 ]


print("Even =",evens)
print("Odd =",odds)
print("===============")


# count frequency
lst=[1,2,4,5,6,7,4,3,2]
target=7
print(lst)
print(f"Frequency of {target} =" ,lst.count(7))
print("=====================")


# sum and average of list
lst=[1,2,4,5,6,7,4,3,2]
total_sum=sum(lst)
average=total_sum/len(lst)
print(lst)
print("Sum =",total_sum)
print("Average =",average)
print("================")


# comman elements in two list
list1=[1,2,6,7,4]
list2=[2,4,5,3,8]
comman=list(set(list1) & set(list2))
print("Comman Elements =",comman)
print("============")

# missing element in first n elements
lst=[1,2,3,5,6]
n=len(lst)+1
expected_sum=n*(n+1)//2
actual_sum =sum(lst)
missing_number=expected_sum - actual_sum
print("Missing Number =",missing_number)
print("===================")


# sort ascending without sort()
lst = [64, 34, 25, 12, 22, 11, 90]
n = len(lst)

for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Sorted List:", lst) 