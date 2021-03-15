a=int(input())
i=2
s=0
S=""
for i in range(2,a+1):
    x=str(i)
    y=str(i+1)
    s=s+(i*(i-1))
    S=S+x+"*"+y
    i=i+1