m = [
    [1,2,3,"a"],
    [4,5,6,"b"],
    [7,8,9,"c"],
    [10,11,12,13 ]
    ]


n = []

row,column ,rotate = 4 ,4,1#map (int,input().split())
for k in range(rotate):
    for i in range(row):
        for j in range( column):
            m[j-1][i] = m[j][i] 
            
            
print(m)
            
            
            
            