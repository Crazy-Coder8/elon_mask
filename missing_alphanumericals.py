

s = "12393uday"


nn = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
aa= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z"]

for i in s:
    if i in nn:
        nn.remove(i)
    else:
        aa.remove(i)
print("".join(nn)+''.join(aa))

"""

1)

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
"""

""""
2)


def MissingCharacters(s):
    
    l= [0]*123
    result= " "
    for i in range(len(s)):
        x= ord(s[i])
        l[x]+=1
    for i in range(48,58):
        if(l[i ]==0):
            result+=chr(i)
            
    for i in range(97,123):
        if (l[i]==0):
            result+=chr(i)
    return result

s = "12393uday"
print(MissingCharacters(s))

"""














