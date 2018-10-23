#a class called employee is created
class Employee:
    empCount=0
    #parameterized constructor
    def __init__(self,name,desig,salary):
        self.name=name
        self.desig=desig
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("There are %d employees" % Employee.empCount)
    def displayDetails(self):
        print("Name is",self.name, "Designation is",self.desig,"Salary is",self.salary)

e1=Employee("Faran","Manager",100000)
e2=Employee("Mike","Team Lead",50000)
e3=Employee("Narayanan","Programmer",40000)
e4=Employee("Nigam","Programmer",50000)
e4.displayCount()
e2.displayDetails()
