class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        params = string.split('-')
        return cls(params[0] , params[1] , params[2])

    @classmethod
    def from_str2(cls,string):
        return cls(*string.split('-'))

    @staticmethod
    def printgood(string):
        print('this is good ', string)

class Programmer(Employee): # this is single inheritance class, takes all methods from Employee.
    no_of_holiday=22
    def __init__(self, aname, asalary, arole, alanguage):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = alanguage

    def printprog(self):
        return f'The programmers name is {self.name}. Salary is {self.salary}. Role is {self.role}, and know {self.language}'



ramesh = Employee('Ramesh',1000,'Boss')
gordon = Employee("Gordon", 100, "instructor")
jino = Employee.from_str('Jino-400-chef')
candadai = Employee.from_str2('raghu c-1000-AVP')

subham = Programmer('Subham', 999, 'Programmer',['Python','Java'])
karan = Programmer('Karan',777,'Programmer',['Python','C#'])
print(karan.printprog())
print(karan.printdetails())
print(karan.no_of_holiday)