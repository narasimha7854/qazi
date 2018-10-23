class ABC() :
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print("Var1 is",self.var1)
        print("Var2 is",self.var2)

obj=ABC(10,12.34)
obj.display()

print("Object dictonary is",obj.__dict__)
print("Objects documentation",obj.__doc__)
print("Class name is",ABC.__name__)
print("Object module is",obj.__module__)
print("Class Base is",ABC.__bases__)
