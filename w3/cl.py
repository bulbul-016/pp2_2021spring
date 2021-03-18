class Person:
    def f(self):
        print(f"name: {self.name}, sname:{self.sname}")
p1=Person()
p1.name="Baby"
p1.sname="Girl"

p2=Person()
p2.name="baby"
p2.sname="girl"

p1.f() #name: Baby, sname:Girl
p2.f() #name: baby, sname:girl

Person.f(p1) #name: Baby, sname:Girl
Person.f(p2) #name: baby, sname:girl