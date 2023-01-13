for i in range(int(input())) : 
    n = int(input())
    l = list(map(int,input().split()))
    c =l[0]

    b= 1 

    for i in range(1,len(l)):
        if c > l[i] : 
            b += 1 
        c=l[i]
        
    
    print(b)   
    
    for _ in range(int(input())):
    a = int(input())
    l = list(map(int,input().split()))
    c = 1
    b = l[0]
    for i in range(1,a):
        if l[i]<= b:
            c+=1
            b = l[i]
        
    print(c)