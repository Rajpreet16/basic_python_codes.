#Create integer set from list and character set. Perform following functions on the same:  update(), discard(),  pop() and intersection()

int_set.update(['3','4'])
print(int_set)
int_set.discard('4')
print(int_set)
int_set.pop()
print(int_set)
print(int_set.intersection(char_set))

print("---------------------------------------------")