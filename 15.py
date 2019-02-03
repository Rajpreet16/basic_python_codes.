#Write a Python Program to check string entered by user is palindrome or not.

def reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev = reverse(s)

    if(rev == s):
        print("Yes")
    else:
        print("No")

s = input()
isPalindrome(s)
