arr = [7, 5, 3, 2]
n = 4
brr= [5, 4, 8, 7] 
arr.sort()
brr.sort()
count = 0
for i in range(n ) : 
    if arr[i] >= brr[i] :
        count +=1
        
if count >0 :
    print("NO")

else:
    print("YES")        