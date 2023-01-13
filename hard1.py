
from itertools import permutations

l = []

a = 2
b = 2
for i in range(a):
    l.append("1")
    
for i in range(b ):
    l.append("0")
    

c= 0
p = permutations(l)
for i in list(p):
    if list(i) == list(i).reverse() :
        c+=1

print(c)