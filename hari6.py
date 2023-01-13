n,m,k = map(int,input().split())
count = 0
for i in range(n):
    
   l = list(map(int,input().split()))
   a = sum(l[:-1])
   if a > m  and l[-1] < 10:
       count +=1
       
print(count)