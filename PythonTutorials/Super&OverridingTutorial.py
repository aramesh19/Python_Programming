class A:
    classvar1 = 'I am a class variable in class A'
    def __init__(self):
        self.var1 = 'I am inside class A\'s constructor'
        self.classvar1 = '\nInstance variable in class A'
        self.special = "\nspecial"

class B(A):
    classvar2 = 'I am in class B'
    def __init__(self):
        #super().__init__() #  this calls the constructor of the super class.
        self.var1 = "\nI am inside class B's constructor"
        self.classvar1 = "\nInstance variable in class B"
        super().__init__()
        print(super().classvar1)

a = A()
b = B()

print(b.classvar1)
print(b.special, '\n',b.var1,'\n',b.classvar1)


