import re

txt = "ahe rain in Spaib"

x = re.findall("[a-z]", txt) 
u = re.findall("[A-Z]", txt) 
a = len(x)+len(u) # 8 or more char

y = re.findall("\Aa", txt) # a-at the beginning 

z = re.findall("b\Z", txt) # b-in the end

if z and y and a>8:
    print("yes")
else:
    print("no")