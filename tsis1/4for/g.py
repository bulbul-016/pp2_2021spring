a=int(input())
b=int(input())
n=1
for i in range(1,a+1):
    n=n*i
    i=i+1
k=1
for j in range(1,b+1):
    k=k*j
    j=j+1
o=1
for l in range(1,((a-b)+1)):
    o=o*l
    l=l+1
r=n/(k*o)
print(int(r))
'''
4
2

6
'''