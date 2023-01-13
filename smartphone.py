

n = int(input())
max = 0 
l = []
for i in range(n):
    l.append(int(input()))
    
l.sort()

    
for i in range(n):
    sum = l[i]*(n-i)
    if sum > max :
        max = sum 
        
print(max)