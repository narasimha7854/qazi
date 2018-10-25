#a function that returns two results

def sum_sub(a,b):
    """this function returns results of addition and substraction"""
    c=a+b
    d=a-b
    return c,d
#get the results from the function
x,y=sum_sub(10,5)
print('Result of Addition',x)
print('Result of Substraction',y)