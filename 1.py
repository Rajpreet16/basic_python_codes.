#Create list of integers and convert it into ByteArray.

list1 = [1,2,3,4,5]
list1 = bytearray(list1)
print(list)

#Create range of first 10 integers and Create list of odd integers from 3 to 15 using range.

range1 = range(0,10)
print(range1)
list2 = list(range(3,16,2))
print(list2)

#Create integer set from list and character set. Perform following functions on the same: add(), remove(), and union().

list3 = ['1','2','3','4','5','a','b','c','d','e']
int_set = set({})
char_set = set({})
final_set = set({})
intersection_set = set({})

for x in list3:
    if x.isalpha()==True:
        char_set.add(x)
    if x.isdigit()==True:
        int_set.add(x)

print(int_set)
print(char_set)

final_set = int_set.union(char_set)
print(final_set)

int_set.remove('1')
print(int_set)

# Create integer set from list and character set. Perform following functions on the same:  update(), discard(),  pop() and intersection()

int_set.update('6','7')
print(int_set)

int_set.discard('7')  
print(int_set)

print(int_set.pop())  

intersection_set.intersection(int_set,char_set)
print(intersection_set)

#Implement following string functions: replace(), count(), capitalize(), and join().
import string

string1 = "pingma"
string2 = "--"
print(string1)

string1 = string1.replace("p","ee")
print(string1)

print(string1.count("e"))

string1 = string1.capitalize()
print(string1)

string2 = string2.join(string1)
print(string2)


#Create a list of integers, mixed data types, duplicate data items and nested lists.


list4 = [1,2,3,4,5]
print(list4)

list5 = [1,2,3,"enigma",4.0]
print(list5)

list6 = [[1,2,3],[4,5,6],[7,8,9]]
print(list6)
print(list6[0][2])

for x in range(len(list6)):
    for x1 in range(len(list6[x])):
        print(list6[x][x1])

import itertools
list7 = ['e','n','i','g','m','a']
list8 = list(itertools.chain.from_iterable((e,e) for e in list7))
print(list8)


#Perform list methods: append(), insert() and remove().

list8.append('a')
print(list8)

list8.insert(0,'E')
print(list8)

list8.remove('E')
print(list8)

#Show that lists are mutable.

list9 = [1,2,3,4,5,6,7,8,9]
list9[0]=0
print(list9)

#Perform list methods: extend(), pop(), index(),  count() and sort().
list9 = ['a','a','a']
list8.extend(list9)
print(list8)

print(list8.index('a',-1))

list8.sort()
print(list8)


#Create tuple consisting of months.
tuple1 = ("Jan","Feb","MAr","April","May","June","July","August","Sept","Oct","Nov","Dec")
print(tuple1)

# Show that tuple is immutable.
#tuple1[0]="lol"
#print(tuple1)

#Perform tuple functions such as: all(),  max(), sorted() and sum().

print(all(tuple1))
print(max(tuple1))
print(sorted(tuple1))

tuple2 = (1,2,3,4,5,6,7,8,9,10)
print(sum(tuple2))

# Create dictionary of fruit names and its colors.

dic1 = {"Apple":"Red","Orange":"Orange","Kiwi":"Brown","Banana":"Yellow"}

print(dic1.pop("Apple"))
print(dic1.get("Brown"))
print(dic1.keys())
print(dic1.values())
print(dic1.update({"Pomegranate":"Red"}))
print(dic1)

#Create character array and use following functions: append(), insert(), remove(), pop(), reverse(), sort() and count().
from array import *

arr1 = array('u',['e','n','i','g','m','a'])
for x in range(0,len(arr1)):
    print(arr1[x],end="")
print("\n")

arr1.append("a")
for x in range(0,len(arr1)):
    print(arr1[x],end="")
print("\n")

arr1.insert(0,"E")
for x in range(0,len(arr1)):
    print(arr1[x],end="")
print("\n")

arr1.remove("E")
for x in range(0,len(arr1)):
    print(arr1[x],end="")
print("\n")

print(arr1.pop())

arr1.reverse()
print(arr1)

print(arr1.count("e"))






