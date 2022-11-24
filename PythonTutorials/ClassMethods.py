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




ramesh = Employee('Ramesh',1000,'Boss')
gordon = Employee("Gordon", 100, "instructor")

print('Gordon Salary: ', gordon.salary)
print('Leaves before change: ', ramesh.no_of_leaves)

ramesh.change_leaves(15)

print('Leaves after change: ', ramesh.no_of_leaves)