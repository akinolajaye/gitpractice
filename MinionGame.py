def minion_game(string):
    

    vowels="AEIOU"


    

    
    kevin=0
    stuart=0
    
    for i in range(len(string)):
        
        
        
        if string[i] in vowels:
            

            kevin+=(len(string)-i)

        else:
            stuart+=(len(string)-i)
                


    if kevin >stuart:
        print(f"Kevin {kevin}")
    elif kevin==stuart:
        print("Draw")
    else:print(f"Stuart {stuart}")
        

    

        

if __name__ == '__main__':
    s = input()
    minion_game(s)