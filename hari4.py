for i in range(int(input())):
    s =input()
    t = input()
    m= ""
    for i in range(5):
        if s[i] == t[i] :
            m+="G"
            
        else:
            m+="B"
            
    print(m)
         
              