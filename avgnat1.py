print(" Claculate Average of the first n natural numbers")
n=int(input("Enter which of the number below average"))
avg=0.0
s=0
for i in range(1,n+1):
    s=s+i
    avg=s/i
print("The sum of First ",n,"natural number is",s)
print("The average of first",n,"natural number is",avg)
print("**********************")
