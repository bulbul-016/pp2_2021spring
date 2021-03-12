a=int(input())
if a>=1440:
    b=a-(24*60)
    print(int(b/60))
    print(int(b%60))
elif a<1440:
    print(int(a/60))
    print(int(a%60))
#partial solution