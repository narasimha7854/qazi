#to find the occurance
str=input("Enter a String")
sub=input("Enter Sub String")

#find the position of sub string
n = str.find(sub,0,len(str))

if n== -1:
    print("Sub String not found")
else:
    print("Sub String found at position:",n+1)
