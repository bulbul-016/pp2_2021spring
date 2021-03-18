class Person:
    def __init__(self, fname, lname):
        print("parentss")
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname):
        print("childss")
        Person.__init__(self,fname, lname)
x=Student("Bulbul" , "Qassymbek")
x.printname()
'''
childss
parentss
Bulbul Qassymbek
'''