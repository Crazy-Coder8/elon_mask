def f (l):
    p = set(l)
    h = [] 
    for i in p:
        h.append(l.count(i))
        
    s = max (h)    
    h.remove(max(h))
    if s in h :
        print("NO")
    else:
        print("YES")
        
        
for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    f(l)
    
    
        
        