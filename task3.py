if __name__ == "__main__":
    from random import choice                                                                  #importing choice from random
    def chat():                                                                                #defining chat function
        '''This program makes a chat system of the University'''
        print("Welcome to Pop Chat\nOne of our operators will be pleased to help you today.\n")
        university_email=input("Please enter your University of Poppleton email address: ")    #asking student to enter their email address
        position=university_email.index("@")                                                   #storing the position of '@'

        #Tuple to store the options and the response to those options
        options_choose=((["wifi","network"],("WiFi is excellent across the campus.")),(["library","book"],("The library is closed today.")),
        (["ending","deadline"],("Your deadline has been extended by two working days.")),
        (["parking","vehicle"],("Parking is free inside the building")),(["classroom","room"],("Its on the right side of the library")),
        (["lab","research"],("Its on the next floor")),(["canteen","food"],("Its on the ground floor")))
        
        responses=["Hmmm","Oh, yes, I see","Tell me more","Really","Intresting","Sure"]        #creating list for responses
        ending_message=["exit","bye","quit","goodbye","end","help"]                            #creating list for end meaasage        
        error_list=[1,1,1,1,1,0,1,1,1,1]                                                       #creating list for Network Error part
        random_number=choice(error_list)                                                       #choosing random number form error_list
        
        if university_email.count("@")==1 and university_email[position+1:] =="pop.ac.uk":     #checking condition for email address
            name=university_email[:position]                                                   #storing name of student before '@' in name
            first_name=name.capitalize()                                                       #capitalizing the name
            print(f"Hi,{first_name}! Thank You, and Welcome to PopChat!")
            names=["Jack","Jhon","Alex","Harry","Janice","Fiona"]                              #creating another list for random names
            random_name=choice(names)                                                          #vhoosing any random name
            print(f"My name is {random_name}, and it will be my pleasure to help you.")  

            while True:                                                                        #while true this runs
                if random_number == 0:                                                         #if condition for network error
                    print("*** NETWORK ERROR ***")  
                    break
                question =input("---> ")                                                       #asking input from user
                spliting=question.split()                                                      #spliting user input
                if question.lower() in ending_message:                                         #checking if input is in list of ending message
                    break                                                                   
                
                for i, j in options_choose:                                                    #looping on options_choose tuple
                    if (i[0] in spliting or i[1] in spliting):                                 #checking the condition 
                            print(j)                                                           #printing the 'j' part which stores the message
                            break    
                else:                                                                          #if not for loop else part will run
                    print(choice(responses))                                                   #printing random choices
            print(f"\nThanks, {first_name}, for using PopChat. See you again soon!")
        else:                                                                                  #if condition of email address doesnot matches
            print("Email address not valid!")
            exit()
    chat()                                                                                     #calling the function
