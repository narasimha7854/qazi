#class circle

class Circle:
    PI=3.1415
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return Circle.PI*self.radius*self.radius
    def circumference(self):
        return 2*Circle.PI*self.radius
    def display(self):
        print("Area is",c.area())
        print("Circumference is", c.circumference())

c=Circle(7.5)
c.display()
