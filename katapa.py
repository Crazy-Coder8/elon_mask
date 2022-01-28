
o =0
e =0
l= []
for  _ in range(int (input())):
    l.append(int(input()))
for i in l :
     if i %2 ==0 :
         e +=1

     else :
          o += 1

if e>o :
    print("READY FOR BATTLE")
else :
    print( "NOT READY")



