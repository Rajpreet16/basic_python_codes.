#Write a Python Program to create phone book with names and phone numbers.

with open("phonebook.dat","wb") as f:

    n = int(input("Entr Number of Entries"))

    for i in range(n):
        name=input('enter name :')
        phone=input('enter no.')
        name=name.encode()
        phone=phone.encode()
        f.write(name+phone)
