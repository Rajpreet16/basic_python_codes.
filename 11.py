#Write a python program to make a simple calculator that perform add, subtract, multiply and division operations.

def add(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def div(x,y):
    return(x/y)

def mul(x,y):
    return(x*y)


a = int(input("Enter A:"))
b = int(input("Enter B:"))

print(add(a,b))
print(sub(a,b))
print(div(a,b))
print(mul(a,b))
