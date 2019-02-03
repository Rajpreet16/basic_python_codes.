#Write a python program to find the Factorial of a number.

def fact(x):
    if(x>=1):
        return x*fact(x-1)
    else:
        return 1

num = int(input("Enter Number"))
fa = fact(num)
print(fa)
    
