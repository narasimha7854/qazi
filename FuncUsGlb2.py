#accessing the global variable
num=100
def myfunc():
    global num
    print('The Global Variable is',num)
    num=200
    print('Modified Variable value is',num)

myfunc()
print('The variable value is',num)

