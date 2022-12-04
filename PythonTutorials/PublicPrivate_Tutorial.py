class Employee:
    no_of_leaves = 8
    var=8
    _compensation = 1000 ## protected variable, can used in child or sub classes.
    __PrivCompensation = 1500 ## private variable, can be accessed with _ClassName__VariableName

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

class Player:
    no_of_games = 4
    var = 9
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f'Name is {self.name} and game is {self.game}'

class CoolProgrammer(Employee,Player):
    language = 'C#'
    var=10
    def printlanguage(self):
        print(self.language)


ramesh = Employee('Ramesh',1000,'Boss')
gordon = Employee("Gordon", 100, "instructor")


print(gordon._compensation)
print(gordon._Employee__PrivCompensation)

