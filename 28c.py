n,k = map(int, input().split())
f = list(map(int, input().split()))
c = 0 
for i in range(n) :
    j=1
    while (j< n):
        if f[i]-f[j] >= k:
            c+=1
        j +=1
        
        
        
print(c)