

string = 'ABCDCDC'
sub_string='CDC'
s = len(string)
sb = len(sub_string)
"""
for i in range(s):
        for j in range(i+1,s+1):  
                l.append(string[i:j])
                
"""

l =[string[i:j] for i in range(s) for j in range(i+1,s+1)]

print(l.count(sub_string))




    
        