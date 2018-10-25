#To find what least number to nust add to get perfect division

#run time input
divd=int(input("Enter dividend1 number:"))
divs=int(input("Enter Divisor1 number :"))

print("What is least number must be add to get exact division")

#calculate remainder and get remainder
rem= divd%divs
print("you can add",rem,"to get perfect divisable" )

#after getting remainder substract remainder from dividend
#get quotient
qust=(divd-rem)/divs
#divd=(divs*qust)+rem
print("After adding least number exact divisible number is:",qust)

