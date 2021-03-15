def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) #lambda a: a*2
mytripler = myfunc(3) #lambda a: a*3

print(mydoubler(11)) 
print(mytripler(11))

#22
#33