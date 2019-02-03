# Write a python program to implement lambda with reduce function to calculate products of elements of a list.
from functools import *

product = [1,2,3,4,5,6,7,8,9]
product = reduce(lambda a,b:a*b,product)
print(product)

#Write a python program to find GCD of two numbers.

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a = int(input())
b = int(input())

print(gcd(a,b))
