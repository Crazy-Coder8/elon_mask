l = [3 ,2 ,2,1]
s = set (l)
d = []
c = 0 
for i in s:
    j = l.count(i)
    if c<j:
        d.append(j)
        
        
if len(s) == len(set(d)):
    print("True")
else:
    print("False")
