import re

file=open('in_the', 'r')
text=file.read() #my babygirl

x=re.search('my', text)
print(x) #<re.Match object; span=(0, 2), match='my'>

if (x): print("YES") #YES
else: print("NO")