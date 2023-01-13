n , k = map(int, input().split())
f = list(map(int, input().split())) 
c =0 
for i in range(n):
    for j in range(n):
        if i!= j and f[i] + f[j] <k :
            c += 1 
            
            
print(int(c/2))
             