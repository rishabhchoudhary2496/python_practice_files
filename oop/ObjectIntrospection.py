import inspect
class Employee:
    id = 102
    def __init__(self,fname,lname) -> None:
        self.fname = fname
        self.lname = lname


    def explain(self):
        if self.fname == None or self.lname==None:
            return 'first and last name not set'
        return f'This employee {self.fname} {self.lname}'

    @property
    def email(self):
        if self.fname == None or self.lname==None:
            return 'Email not set'
        return f'{self.fname}.{self.lname}@company.com'

    @email.setter
    def email(self,email):
        self.fname,self.lname = email.split('@')
        print(self.fname)
        self.explain()

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

    def printInstanceVariable(self):
            return inspect.getattr_static(self,'fname')


from pprint import pprint
d = Employee('Ail','sle')
e = Employee('Dale','Ali')
print(type(d))
print(id(d))
pprint(d.printInstanceVariable())