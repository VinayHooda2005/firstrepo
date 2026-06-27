# # string indexing 
# text=("hello,world")
# print(text[3])   
# print(text[7])
# print(text[-3])


# string slicing
text=("hello,world")
print(text[::4])
print(text[3:7])
print(text[1:9:2])
print(text[:5])
print(text[6:])


# # changing the cases of string
# name="VInay"
# print(name.upper())
# print(name.lower())
# print(name.capitalize())

# title="python programming"
# print(title.title())


# # trimming whitespace
# name="    vinay   "
# print("|" + name.strip() + "|")
# print("|" + name.lstrip() + "|")
# print("|" + name.rstrip() + "|")


# # search and replace
# text="hello,world"
# print(text.replace("hello", "hi"))

# find_text="hello,world"
# print(find_text.find("world"))

# rfind_text="hello,world"
# print(rfind_text.rfind("l"))


# # splitting and joining strings
# text="hello world"
# print(text.split(" "))

# join_text=["hello", "world"]
# print(" ".join(join_text))