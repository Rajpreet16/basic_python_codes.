#Write a Python Program to print all Prime Numbers in an Interval.

l = int(input())
u = int(input())

for x in range(l,u+1):
    if x >1:
        for i in range(2,l):
            if(x%i)==0:
                break
        else:
            print(x)


