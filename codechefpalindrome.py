
from itertools import permutations

for _ in range(int(input())):
    a, b = map(int, input().split())
    l =[]
    for i in range(a):
       l.append("1")
    
    for i in range(b ):
        l.append("0")
        

    c= 0
    p = permutations(l)
    for i in list(p):
        k = list(i)
        if k == k[::-1]:
            c +=1
            
        if c ==2 :
            break 

    if c== 2 :
        print("YES")
    else:
        print("NO")  