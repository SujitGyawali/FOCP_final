print("Stop! Who would cross the Bridge of Death\nMust answer me these questions three,'ere the other side he see.")
name=input("What is your name? ")              #Asking name from the user
if name=="Arthur" or name=="arthur":           #checking name for Arthur
    print("My Liege! You may pass!")
else:                                          #if name is other than Arthur
    seek=input("What do you seek? ")   
    if seek!="Grail" and seek!="grail":        #checking seek condition
        print("Only those who seek the Grail may pass.")
    elif seek == "Grail" or seek == "grail":   
        colour=input("What is your favourite colour? ")
        if colour[0].upper()==name[0].upper(): #checking the first character of name and colour is same
            print("You may pass!")
        else:                                  #if condition is fasle  
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
