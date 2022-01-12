score1 ,score2, lead = 0,0,0
for _ in range (int(input(" Enter the number of rounds : "))):
    try :
        a,b = map(int,input("Enter the players score (space seperated) : ").split())

    except:
        print(""" GIVE A SPACE AFTER THE FIRST VALUE 
                   ... LAST ROUND NOT RECORDED.....


                """)

    


    score1 +=a
    score2 +=b
    if a>b and abs(a-b)>0 :
        winner = 1
        if abs(a-b) >lead :
            lead = abs(a-b)


    else :
        winner = 1
        if abs(b-a) > lead :
            lead = abs(b-a)



print( "The is  winner ",winner ,"and the lead is " ,lead)

        

