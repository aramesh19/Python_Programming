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

ramesh = Employee('Ramesh',1000,'Boss')
gordon = Employee("Gordon", 100, "instructor")
jino = Employee.from_str('Jino-400-chef')
candadai = Employee.from_str2('raghu c-1000-AVP')

print(jino.name)
print(candadai.name)

# print('Gordon Salary: ', gordon.salary)
# print('Leaves before change: ', ramesh.no_of_leaves)
#
# ramesh.change_leaves(15)
#
# print('Leaves after change: ', ramesh.no_of_leaves)