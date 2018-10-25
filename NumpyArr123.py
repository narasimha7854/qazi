import numpy as np

a=np.array([1,2,3,4,5],float)
print(a)

b = np.array([[1,2,3],[4,5,6]])

print(b)
print(b[:,2])
print(b.dtype)
print(b.shape)

c=np.array(range(10),float)
print(c)

arr1=np.array([1,2,3],float)
arr2=arr1
arr3=arr1.copy()
print(arr1)
print(arr2)
print(arr3)

ar4= np.array(range(6),float).reshape((2,3))
print(ar4)
print(a.transpose())

ar5=np.array([[1,2,3],[4,5,6]],float)
print(ar5)
print(a.flatten())


ar6=np.array([[1,2],[3,4]],float)
ar7=np.array([[5,6],[7,8]],float)
print(np.concatenate(ar6,ar7))






