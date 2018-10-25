#global variable
a=10
def myfunction():
    a=20
    print('the value of a is',a)   #displays the local variable

myfunction()
print('The value of a is',a) # calls the global variable

