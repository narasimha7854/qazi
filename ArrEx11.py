from array import *
#accept marks as string
str= input('Enter marks').split(' ')

#store the marks into marks array
marks=[int(num) for num in str]

#display the marks and find total
sum=0
for x in marks:
    print(x)
    sum+=x
print('Total Marks are',sum)

#display percentage
n = len(marks)
percent=sum/n
print("Percentage: ",percent)