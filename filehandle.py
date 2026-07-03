# read text in text.txt file
f=open("text.txt","r")
print(f.read())
f.close()

# write text in text.txt file
f=open("text.txt","w")
f.write("hello,where are you going")
f.close()

# to make file with python code
import os
open("file.txt","w")

# to remove file with python code
os.remove("file.txt")

# to make file with python code and add name ,course
import os
open("student.txt","w")

f=open("student.txt","w")
f.write("name:vinay  course:python")

# to add text in student file
f=open("student.txt","a")
f.write("  city:rohtak")

# to read file
f=open("student.txt","r")
print(f.read())
f.close()

# to create folder 
# os.mkdir("poria")

#to find lines in file
f=open("student.txt","r")
print(len(f.readlines()))