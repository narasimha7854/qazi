def sum_sub_mul_div(a,b):
    """This function returns the result of addition"""
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    return c,d,e,f

#get result from sum_sub_mul functions and store into t
t=sum_sub_mul_div(10,2)

#display the result using for loop
print('The results are')
for i in t:
    print(i, end=' ')
    