#Create a list of integers, mixed data types, duplicate data items and nested lists.

#mix data type 
listt = [1,2,3,4.0,5.0,"Enigma",1,2,3,[6,7,8]]
print(listt)

#duplicate list
l = ['a','b','c','d']
l1 = l
print(l1)

listt1 = [[1,2,3],[4,5,6],[7,8,9]]
for x in range(len(listt1)):
    for x1 in range(len(listt1[x])):
        print(listt1[x][x1])


