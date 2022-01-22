if __name__=="__main__":
    from statistics import mean                           #importing mean
    print("Sallow Speed Analysis: Version 1.0")           

    def reading():                                        # defining reading function
        '''To find the maximum speed, minimum speed and the average speed of the Swallows in UK and in Europe.'''

        swallow_speed=[]                                  #declaring empty list
        counter=0                                         #counter variable is declared to store readings

        while True:                                       #if the condition true this runs
            user_input=input("Enter the Next Reading: ")  #asking input from user
            if user_input=="" and counter>=1:             #checking condition for user_input and length of list
                print("\nResult Summary\n")
                break
            elif user_input!="":                          #if user_input is not empty this part will run
                print("Reading Saved.")
                if user_input.startswith("E"):            #if user_input first letter starts with 'E' this will run
                    store=float(user_input[1:])/1.60934   #converting kph to mph and storing except first character in store 
                    swallow_speed.append(store)           #appending value of store to list
                    counter+=1                            #increasing the counter by 1

                elif user_input.startswith("U"):          #if user_input first letter starts with 'U' this will run
                    store=float(user_input[1:])           #storing except first character in store converting to float
                    swallow_speed.append(store)           #appending value of store to list
                    counter+=1                            #increasing the counter by 1
            
            else:                                         #if no any user_input is given and swallow_speed is 0 this will run
                print("\nNo readings entered. Nothing to do.\n")
                break

        print(counter," Reading Analysed.") if counter==1 else print(counter," Readings Analysed.") if counter>1 else print(exit())    #ternanry operator

        if swallow_speed!=[]:                             #checking whether list is empty or not
            Max_value=max(swallow_speed)                  #taking out the maximum value
            print(f"Max Speed: {Max_value:.1f} MPH, {Max_value*1.60934:.1f} KPH.")    
            Min_value=min(swallow_speed)                  #taking out minimum value
            print(f"Min Speed: {Min_value:.1f} MPH, {Min_value*1.60934:.1f} KPH.")
            Avg_value=mean(swallow_speed)                 #taking out average value
            print(f"Avg Speed: {Avg_value:.1f} MPH, {Avg_value*1.60934:.1f} KPH.")

    reading()                                             #calling the function
