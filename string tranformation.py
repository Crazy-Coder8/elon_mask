def string_transformation(string):

    d=""
    # we have to divide a space seperated string
    s = list(string.split(" "))
    for i in s:
        for j in range(len(i)):
            if j == 0:
                d+=i[j] 
                
            elif ord(i[j-1]) < ord(i[j]):
                d+=i[j].upper()
                
            elif ord(i[j-1]) > ord(i[j]):
                d+=i[j].lower()
                
                
            elif ord(i[j-1]) == ord(i[j]):
                d+=i[j]
                
            
                
                            
        d+=" "
        
    return d
            
    """_summary_
    """    
 

print(string_transformation("a Blue MOON"))