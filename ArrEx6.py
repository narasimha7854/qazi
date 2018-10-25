#operations on array
from array import *

#create an array with integer values

arr=array('i',[10,20,30,40,50])
print('Original Array is',arr)

#append the array
arr.append(30)
arr.append(60)
print('After Appending 30 and 60',arr)

#insert 99 at position number
arr.insert(1,99)
print('After inserting 99 in 1st position',arr)

#remove the last element using pop()
n=arr.pop()
print('After poping the items',arr)
print('Popped elements',n)
