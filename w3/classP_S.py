class Person:
    def f(self, name, age):
        self.name=name
        self.age=age
        print("Person created")
    def say_hello(self):
        print(f"{self.name} says hello")
class Student(Person):
    def s(self):
        print(f"{self.name} studies")

class Teacher(Person):
    def t(self):
        print(f"{self.name} teaches")

s1 = Student("Miko", 19)
t1 = Teacher("Baby", 44)

s1.say_hello()
s1.s()