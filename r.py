class CSE:
    count = 0 
    def __init__(self,name,roll,college):
        self.nm = name
        self.rll = roll
        self.col= college
        self.count += 1
        
        
        
        
    def __str__(self):
        return self.nm + "  "+str(self.rll)+"  "+self.col
    
    
    def lst(self):
        return (self.nm,self.rll,self.col)
    
        
        
        
        
        
        
     
        
uday = CSE("uday", 28,"kucet")
hari = CSE("hari",41,"mrnc")
print(uday)
print(uday.lst())