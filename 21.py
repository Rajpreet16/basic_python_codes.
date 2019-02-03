#Write a Python Program to create a binary file and store a few records.

reclen = 20

with open("city.bin","wb") as f:
    n = int(input("Enter Number of Entries"))

    for i in range(n):
        city = input("Enter City")
        ln = len(city)
        city = city+(reclen-ln)*' '
        city = city.encode()
        f.write(city)

with open("city.bin","rb") as f:
    n = int(input("Enter The Record Number"))
    f.seek((reclen*(n-1)))
    str1 = f.read(reclen)
    print(str1.decode())
