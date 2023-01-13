import re as r



T = int(input())
for i in range(T):
    f = int(input())
    s= input()
    d = r.findall("START38",s)
    print(len(d),f-len(d))
    
    
    