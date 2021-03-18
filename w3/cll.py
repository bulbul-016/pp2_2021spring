class Person:
    def f(self , n):
        for i in range(n):
            print(f"name: {self.name}, sname:{self.sname}")

p1=Person()
p1.name="Baby"
p1.sname="Girl"

p2=Person()
p2.name="baby"
p2.sname="girl"

p1.f(3)
'''
name: Baby, sname:Girl
name: Baby, sname:Girl
name: Baby, sname:Girl
'''