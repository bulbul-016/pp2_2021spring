x=int(input())
y=int(input())
z=int(input())
if x+y>z:
    print("YES")
elif y+z>x:
    print("YES")
elif z+x>y:
    print("YES")
else:
    print("NO")
'''
3
4
5
YES
'''