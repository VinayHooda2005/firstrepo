#Right angled triangle
n=5
for i in range(1,n+1):
    print('*'*i)
print("===============")

#Inverted right angled triangle
n=5
for i in range(n,0,-1):
    print('*'*i)
print("===============")

#left angled tiangle
n=5
for i in range(1,n+1):
    print(" "*(n-i),'*'*i)
print("===============")

#Inverted left angled triangle
n=5
for i in range(5,0,-1):
    print(" "*(n-i),'*'*i)
print("===============")

#full pyramid 
n=5
for i in range(1,n+1):
    print(" "*(n-i),'*'*(2*i-1))
print("===============")

#inverted pyramid
n=5
for i in range(n,0,-1):
    print(" "*(n-i),'*'*(2*i-1))
print("===============")

#Diamond pattern
n=4
for i in range(1,n+1):
    print(" "*(n-i),'*'*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i),'*'*(2*i-1))
print("===============")
          
#hollow square
n=5
for i in range(1,n+1):
    if i==1 or i==n:
        print('*'*n)
    else:
        print('*'+" "*(n-2)+'*')
print("===============")


for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
print("===============")

#hollow triangle
n=5
for i in range(1,n+1):
    if i==1 or i==n:
        print('*'*i)
    else:
        print('*'+" "*(i-2)+'*')
print("===============")

for i in range(1,n+1):
    for j in range(1,i+1):
        if i==n or j==1 or i==j:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
print("===============")

#hourglass 
n=4
for i in range(n,0,-1):
    print(" "*(n-i),'*'*(2*i-1))
for i in range(2,n+1):
    print(" "*(n-i),'*'*(2*i-1))
print("===============")

#Incremental number triangle
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#same number per row
n=5
for i in range(1,n+1):
    print((str(i)+" ")*i)
print("===============")

#floyed triangle
n=4
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print()

#number pyramid
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()