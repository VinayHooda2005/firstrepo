#dictionary in python is a collection of key value pairs.
 
my_dic={"name": "vinay", "age": 21, "city": "rohtak"}
print(my_dic)

# to access key value
print(my_dic["name"])

# to modify key value
my_dic["age"]=22
print(my_dic)

# to adding key value
my_dic["country"]="India"
print(my_dic)

# to remove key value 
my_dic.pop("country")
print(my_dic)

# to find lenght 
print(len(my_dic))

#to clear all key value pairs
my_dic.clear()
print(my_dic)

#to show all key
print(my_dic.keys())

#to show all values
print(my_dic.values())

# to show all key and value pairs
print(my_dic.items())




#set is a collection of unique elements in python
set={1,2,3,4,4,5,6}
print(set)

# to add element``
set.add(7)
print(set)

# to remove element
set.remove(4)
print(set)


# to find lenght
print(len(set))


#to clear elemeents
set.clear()
print(set)

# to find union
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1|set2)

# to find itersection
print(set1&set2)