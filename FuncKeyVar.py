def display(farg,**kwargs):
    """to display the values"""
    print("Formal Arguments",farg)

    for x,y in kwargs.items():
        print('Key={}, value={}'.format(x,y))
#pass 1 formal arguments and 2 keyword arguments
display(5,rno=10)
print()

display(5,rno=10,name='Prakash')
