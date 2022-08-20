from sqlite3 import adapt


s = "12393uday"
l = list(s)
ae =[]
ad =[]
nn = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
aa= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z"]
for  i in l:
    if i  in nn :
        ad.append(i)
        
    else:
        ae.append(i)
for i in list(set(ae)):
    aa.remove(i)
    
for i in list(set(ad)):
    nn.remove(i)
    
print(''.join(nn)+''.join(aa))    