for  i in range(int(input())):
    n,m,k = (map(int,input().split())) 
    l = list(map(int,input().split()))  
    count=0 
    for j in range(m):
        if l[j]==1:
            count+=1 
            
    if l.count(1) == n:
        print("100")
        
    elif  count==m:
        print(k)
        
    else:
        print("0")      