
for _ in range(int(input())) :
    a,b,c =map(int,input().split())
    if ( b <c and b>a) or (b >c and b <a ) :
        print (b)

    elif (a>c and a>b ) or (a<c and a>b ) :
        print(a) 

    else :
        print(c)

