class Students:
    def __init__(self,name):
        self.name=name
        #self.tot=tot
       # self.avg=avg
        self.marks=[]
    def enterMarks(self):
        for i in range(3):
            m= int((input("Enter the marks of %s in subject %d:" % (self.name,i+1))))
            self.marks.append(m)
    def total(self):
     return m[0]+m[1]+m[2]

    def average(self):
        return m[0]+m[1]+m[2]/6

    def display(self):
        print(self.name,"got",self.marks)
        print(self.total)
        print(self.average)

s1=Students("Anisha")
s1.enterMarks()
#s2=Students("Rahena")
#s2.enterMarks()***
s1.display()
#***s2.display()***
