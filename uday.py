def su (array,length):
    if len(array) == 0 or len(array) <=3:
        return 0
    else:
        e = []
        o=[]
        for i in range(len(array)):
            if i%2==0:
                e.append(array[i])
            else:
                o.append(array[i])
        e1 =list(set(e))
        o1 =list(set(o))
        e1.sort()
        o1.sort()
        return e1[-2]+o1[-2]
  
arr= [3,2,1,7,5,4]           
a= su(arr,5)    
print(a)
            
            
            
            
            
            
