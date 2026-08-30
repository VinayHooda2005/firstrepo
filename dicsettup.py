# # find highest scorer in student name and marks
# students={
#     "Rahul":80,
#     "Priya":85
# }
# highest_scorer=max(students,key=students.get)
# print(students)
# print("Highest Scorer:",highest_scorer)
# print("===================")


# # check frequency in dictionary
# data={
#     "a":30,"b":43,"c":24,"d":43
#     }
# target_val=43
# frequency=list(data.values()).count(target_val)
# print(f"frequency of {target_val} is {frequency}")
# print("========================")


# # merge two dictionary
# dict1={
#     "a":1,
#     "b":2
# }
# dict2={
#     "c":3,
#     "d":4
# }
# merged_dict=dict1 |dict2
# print("Merged Dict =",merged_dict)
# print("==================")


# # sort by value in dictionary
# scores={
#     "Rahul":80,
#     "Priya":74,
#     "Amit":95,
#     "Sneha":86
# }
# sorted_dict=dict(sorted(scores.items(),key=lambda item:item[1]))
# print("Sorted Dictionary(by value):",sorted_dict)
# print("======================")


# # unique element in list
# lst=[2,4,5,9,2,8,4,3]
# unique_number=list(set(lst))
# print("Unique Number =",unique_number)
# print("================")


# # two sets union, intersection,differeence
# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9}

# union=set1 | set2
# intersection=set1 & set2
# difference=set1-set2
# print("Union (A ⋃ B) =",union)
# print("Intersection (A ⋂ B) =",intersection)
# print("Difference (A-B) =",difference)
# print("======================")


# #convert list to tuple or tuple to list
# my_tuple=(20,20,30,40)
# my_list=list(my_tuple)

# new_tuple=tuple(my_list)
# print("Converted to list =",my_list,type(my_list))
# print("Converted to tuple =",new_tuple,type(new_tuple))
# print("===================")


# # convert dictionary to list of tuple
# data={
#     "Name":"Vinay",
#     "Course":"BCA",
#     "Role":"AI Aspirant"
# }
# list_of_tuple=list(data.items())
# print("List of Tuples:",list_of_tuple)
# print("==================")


# word frequeny counter
text="python is easy to learn and python is powerful"
words=text.split()

word_freq={}
for word in words:
    word_freq[word]=word_freq.get(word,0)+1

print("Word Frequencies:",word_freq)
print("===================")


# phonebook program using dictionary
phonebook = {}

def add_contact(name, number):
    phonebook[name] = number
    print(f"Contact '{name}' added successfully.")

def search_contact(name):
    if name in phonebook:
        print(f"Number for {name}: {phonebook[name]}")
    else:
        print(f"Contact '{name}' not found.")

def show_contacts():
    print("\n--- Phonebook ---")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

# Testing Phonebook functions
add_contact("Vinay", "9876543210")
add_contact("Rahul", "9123456789")

search_contact("Vinay")
show_contacts()