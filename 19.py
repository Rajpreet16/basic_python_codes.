#Write Python program to implement different types of Exceptions.

class myException(Exception):
    def __init__(self):
        print("User Defined Error")

try:
    a = int(input("Enter Number Greater than 10"))
    b = int(input("Enter Number Greater than 0"))
    if b < 10:
        raise myException
    else:
        c = input("Enter String")
        c = a/b
        print(c)

except myException:
    print("User Defined ")
except TypeError:
    print("TYPE ERROR")
except ZeroDivisionError:
    print("?")
    
