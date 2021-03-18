class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name) #Hello my name is John
    print("Hello I am " + str(self.age)) #Hello I am 36

p1 = Person("John", 36)
p1.myfunc()