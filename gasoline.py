
for i in range(int(input())):
    
        n = input()
        l = list(map(int,input().split()))
        g = l[0]
        d= 0

        for i in range(1,len(l)):
            if g == 0 :
                break 
            
            g = g-1+l[i]
            d+=1
            
            
        print(d+g)