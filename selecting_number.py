
"""
l= []

for  i in range(1,):
    s = str(i)
    if s.endswith("3") or s.endswith("2") or s.endswith("9") :
      l.append(s)
      
print(len(set(l)))




"""


for k in range(int(input())):
  l=[]
  a,b  = map(int,input().split())
  for  i in range(a,b+1): 
    s = str(i)
    if s.endswith("3") or s.endswith("2") or s.endswith("9") :
      l.append(s)
  print(len(set(l)))


