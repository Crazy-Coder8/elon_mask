for i in range(int(input())):
    l = list(map(int,input().split()))
    
p = []
for i in range(len(l)):
        count = 0 
        for j in range(len(l)):
            o = abs(l[i]-l[j])
            count+= o 
        p.append(count)
print(min(set((p))))