for i in range(int(input())):
    d,l,r = map(int,input().split(' '))
    if d == l or ( d > l and d < r ):
        print("Take second dose now")
    elif(d>l and d>r) :
        print("Too late")
        
    elif(d<l):
        print("Too Early")