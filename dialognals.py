l = [[1,2,3],[4,5,6],[7,8,9]]
k = len(l[0])
j = []
g = []
for i in range(k):
    j.append(l[k-1-i][i])
    g.append(l[i][i])
    
print(*j)
print(*g)

