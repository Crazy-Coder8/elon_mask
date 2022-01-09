def get_middle(s):
    a = len(s)
    if a %2 == 0 :
        m = s[a/2]
        print(m)
        
    """     
    else :
      s, m = s[a/2],s[a+1/2]
      print(s,m)
    """  


s = "ener"
get_middle(s)
