#a function to calculate factorial value
def fact(n):
    """to find the factorial value"""
    prod=1
    while n>=1:
        prod*=n
        n-=1
    return prod

#to display factorial of first 10 numbers
for i in range(1,11):
    print('Factorial of {} is {}'.format(i,fact(i)))