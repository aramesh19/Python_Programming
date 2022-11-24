class Employee:
    no_of_leaves = 8 ## class variable
    pass

## the objects made out of Employee will share the variables from the class.

harry = Employee()
rohan = Employee()

harry.name = 'Harry'
harry.salary = 10
harry.role = 'Student'
print(harry.__dict__)
harry.no_of_leaves = 10 ## instance variable
## using the above line, the classvariable Employee.no_of_leaves cannot be changed, instead a instance variable gets created.
print(harry.__dict__)
print('Harry Salary: ',harry.salary)

print('No of harry leaves after change: ', harry.no_of_leaves)

rohan.name = 'Rohan'
rohan.salary = 20
rohan.role = 'instructor'
print('No of Rohan leaves: ', rohan.no_of_leaves)
print('No of leaves from Employee class: ', Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 20
print(Employee.__dict__)
print('No of leaves from Employee class: ', Employee.no_of_leaves)
print('Rohan Role: ',rohan.role)