#Write a python program to implement lambda with filter function to filter out even and odd numbers from a list. 

list1 = [1,2,3,4,5,6,7,8,9,0]
print(list1)
list2 = list(filter(lambda var: var%2==0,list1))
print(list2)
list3 = list(filter(lambda var: var%2==1,list1))
print(list3)

#Write a python program to implement lambda with map function that returns squares of elements in a list.

square = list(map(lambda x:x**2,list1))
print(square)
