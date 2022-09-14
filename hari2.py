for _ in range(int(input())):
    n,k = map(int,input().split())
    count = n 
    while(count>=k):
        n = n-k
        count = n
        
    print(count)