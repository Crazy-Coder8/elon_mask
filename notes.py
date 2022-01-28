"""
a= 242

c = 0 
while (a>0) :
    if a>= 100:
        d = int(a/100)
        c +=d
        a = a%100

    elif a>=50:
        d = int(a/50 )
        c += d
        a = a%50

    elif a >= 10 :
        d = int(a/10 )
        c += d
        a = a%10

    else :
        d = int(a/2  )
        c += d
        a = a%2 




print(c)

"""

for _ in range (int (input())) :
    l = [100,50,10,2]
    notes = 0 
    a = int(input())
    for i in l:
        if a >= i:
            notes = notes + int(a/i)
            a = a%i

    print(notes)


