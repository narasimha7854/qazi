#program to find smaller of two numbers using lambda

def small(a,b):
    if(a<b):
        return a
    else:
        return b
sum = lambda x,y : x+y
diff = lambda x,y : x-y
#pass lambda function as argument to regular function
print('Smaller of two numbers',small(sum(-3,-2),diff(-1,2)))