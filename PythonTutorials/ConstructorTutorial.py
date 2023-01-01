class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

## the below line (without #constructor) will throw an error. because the employee class will not take any parameters/arguments
gordon = Employee("Gordon", 100, "Boss")  # arguments sent to class will be handled by init.
## classes can be given arguments via constructors.

print('Gordon Salary: ', gordon.salary)

# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

class Computer:

    def __init__(self, cpu, ram): # normally used to initialize the variables
        print("in init")
        self.capacity = cpu
        self.gb = ram

    def config(self):
        print("Config is: ", self.capacity, self.gb)


com1 = Computer('i5',16)
com2 = Computer('17',32)

com1.config()
com2.config()
