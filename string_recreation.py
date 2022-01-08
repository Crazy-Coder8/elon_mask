"""
replacing the characters as "(" a it not repeated else ")"


"""





def recreate_string(word):

    word .lower()
    output_str = " "
    for i in word :
        if word.count(i) == 1:
            output_str += "("

        else :
    

            output_str += ")"


    print(output_str)









e = input("entr the value :")
recreate_string(e)
























