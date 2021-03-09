def defangIPaddr(address):
    return address.replace('.', '[.]')
a=str(input())
print(defangIPaddr(a))
#1.1.1
#1[.]1[.]1