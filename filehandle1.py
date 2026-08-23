import os
open("file.txt","w")

f=open("file.txt","w")
f.write("Hello !")
f.close()

f=open("file.txt","r")
print(f.read())
f.close()

f=open("file.txt","a")
f.write("Hooda")
f.close()

f=open("file.txt","r")
print(f.read())
f.close()

f=open("file.txt","r")
print(len(f.readline()))
f.close()

os.remove("file1.txt")