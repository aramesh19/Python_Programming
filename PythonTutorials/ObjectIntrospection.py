class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f'{fname}.{lname}@gmail.com'

    def explain(self):
        return f'this employee is {self.fname}  {self.lname}'

    def printemail(self):
        return f'{self.fname}.{self.lname}@gmail.com'

    @property
    def printAddress(self):
        return f'{self.fname} Address is local'

    @property
    def email(self):
        if self.fname or self.lname == None:
            return 'email is not set, please set it using setter'
        return f'{self.fname}.{self.lname}@gmail.com'

    @email.setter
    def email(self, string):
        print('renaming the user names...')
        names = string.split('@')[0]
        self.fname = names.split('.')[0]
        self.lname = names.split('.')[1]

    @email.deleter
    def email(self):
        print('Setting emails to none')
        self.fname = None
        self.lname = None

skillf = Employee('Skill','F')
print(skillf.printemail())
print(type('this is a string'))
print(id('this is a string'))
print(dir('this is a string'))

import inspect
print(inspect.getmembers(skillf))

