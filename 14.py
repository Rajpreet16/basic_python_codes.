#Write a Python Program to Print the Fibonacci sequence

num = int(input())

i = 0
first = 0
second = 1

while(i<num):
    if(i<=1):
        Next = 1
    else:
        Next = first + second
        first = second
        second = Next
    print(Next)
    i=i+1

#Write a Python Program to Check Leap Year

num1 = int(input())

if (num1%4) == 0:
    if(num1%100) == 0:
        if(num1%400) == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("yes")
else:
    print("No")
