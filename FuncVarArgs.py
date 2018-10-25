#variable length arguments
def add(farg,*args):
    # to add given numbers
    print('Formal Arguments',farg)
    sum=0
    for i in args:
        sum+=i
    print('Sum of all numbers=',(farg+sum))

#call add() and pass arguments
add(6,10)
add(5,10,20,40)
