#example on bytearray

elements=[10,20,30,40,50]

#convert the list into byte array type.
x=bytearray(elements)

#modify the first two elements
x[0]=88
x[1]=99

print(x[0])
print(x[1])