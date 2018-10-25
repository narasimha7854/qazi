def square1(x):
    return x*x

num=square1
num2= num(5)+num(6)
num1=num(num(4))

print(num2)
print(num1)

def fxy(f,x,y):
    return f(x)+f(y)
R=fxy(num,2,3)

print(R)

a=0
b=0
def incr(a):
    b=a+1
    return b
z=incr(5)
print(z)

pi=3.14
def area(r):
    return pi*r*r
print(area(2))

numcalls=0
def square3(x):
    global numcalls
    numcalls=numcalls+1
    return x+x
print(square3(4))

print(square3(5))
