for _ in range(int(input())):
    n,k = map(int,input().split())
    if k!=0 :
        print(n%k)
        
    else:
        print(n)
    
    
    
    '''count = n 
    while(count>=k):
        n = n-k
        count = n
        
    print(count)'''