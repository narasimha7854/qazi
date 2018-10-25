
add = lambda x,y: x+y  #lambda function that adds two numbers

#lambda function calling another lambda
mul_an_add = lambda x,y,z:add(y,z)
print(mul_an_add(3,4,5))