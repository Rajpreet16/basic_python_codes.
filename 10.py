#Write a python program to Print Pascal’s triangle for ‘n’ number of rows entered by user.

num = int(input("Enter Number Of Rows"))
a = []

for i in range(num):
    a.append([])
    a[i].append(1)

    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])

    if(num!=0):
        a[i].append(1)


for i in range(num):
    print(" "*(num-1),end=" ",sep=" ")
    for j in range(0,i+1):
        print(a[i][j],end=" ",sep=" ")
    print()
