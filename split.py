""""            def split_and_join(line):
                
                    c = ""

                    b = list(line.split(" "))
                    for i in b:
                        c= c+"-"+i
                    return c[1:]



            if __name__ == '__main__':
                line = input()
                result = split_and_join(line)
                print (result)"""
                
                
                

""""

                def missingCharacters(s):
                    
                    
                            l = list(s)
                            ae =[]
                            ad =[]
                            nn = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                            aa= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z"]
                            for  i in l:
                                if i  in nn :
                                    ad.append(i)
                                    
                                else:
                                    ae.append(i) 
                            for i in list(set(ae)):
                                aa.remove(i)
                                
                            for i in list(set(ad)):
                                nn.remove(i)
                                
                            return str(''.join(nn)+''.join(aa))    
                            
                    
"""


def transformSentence(sentence):
    v = ""
    l = list(sentence.split(" "))
    for i in range(1,len(l)):
        for j in range(len(l[i])+1):
                  print(l[i][j])
        
                

sentence="a Blue MOON"
k ="r"
print(ord("B"))
transformSentence(sentence)