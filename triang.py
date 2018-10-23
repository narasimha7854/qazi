#class circle

class triang:

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def semi(self):
        return triang.a+b+c
    def semi123(self):
        return triang.semi()/2
    def area(self):
        return triang.semi()*((triang.semi()-a)+(triang.semi()-b)+(triang.semi()-c))**0.5

    def display(self):
        print("Area is",self.area())

area1=triang(7,2,6)
area1.display()
