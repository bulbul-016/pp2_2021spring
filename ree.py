import re
txt=input()
x=re.findall("(^.{7}b$)", txt)
if x:
    print("yes")
else: print("no")