# To create file with code
import os
open("example.txt","w")

# To write text in file

f = open("example.txt","w")
f.write("This is a temporary file")
f.close()

# To read file

f = open("example.txt","r")
print(f.read())
f.close()

# To add text in a file

f = open("example.txt","a")
f.write(" , of file handling")

f = open("example.txt","r")
print(f.read())

# To remove file with code

# os.remove("example.txt")

f = open("example.txt","r")
print(len(f.readlines()))