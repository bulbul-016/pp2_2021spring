def f(s):
    print(s)
    '''
    c=len(s)
    while c>0:
        if c==1: return True
        elif c==0: return False
        c=c/2
    '''
t=str(input())
for i in t:
    s=str()
    if i==' ':
        f(s)
        #if f(s)==True: print("H")
        #else: print("C")
    else:
        s=s+i