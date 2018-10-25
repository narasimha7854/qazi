#a python program to access the elements of a string

str='Core Python Programming'

#access each letter using for loop
for i in str:
    print(i, end=' ')
print()  #put the cursor to the next line

#access in reverse order
for i in str[:: -1]:
    print(i, end=' ')