#Create integer set from list and character set. Perform following functions on the same: add(), remove(), and union().

list2 = ['1','a','2','b']
int_set = set({})
char_set = set({})
fset = set({})

for x in list2:
    if x.isalpha()==True:
        char_set.add(x)

    if x.isdigit()==True:
        int_set.add(x)


print(char_set)
fset = int_set.union(char_set)
print(fset)
print("---------------------------------------------")