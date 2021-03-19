lisst=list()
txt=input().split()
for i in txt:
    if int(i)==1:
        lisst.append(i)

for i in txt:
    if int(i)!=1 and int(i)!=0:
        lisst.append(i)

for i in txt:
    if int(i)==0:
        lisst.append(i)
print(lisst)

#1 2 3 5 0 4 0 1 1    3   2
#['1', '1', '1', '2', '3', '5', '4', '3', '2', '0', '0']