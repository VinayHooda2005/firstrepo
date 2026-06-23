# square pattern
for i in range(1, 6):
    for j in range(1,6):
        print("*",end=" ")
    print()


print()
# inverted right triangle pattern
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


print()
# right triangle pattern
for i in range(1,6): 
    for j in range(i):
        print("*",end=" ")
    print()

#number triangle pattern
for i in range(1,7):
    for j in range(1,i):
        print(j,end=" ")
    print()
