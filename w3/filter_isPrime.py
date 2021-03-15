def f(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

list1=[2, 3, 5, 16, 100]
list2=list(filter(f,list1))

print(list2)

#[2, 3, 5]