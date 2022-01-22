import sys
class league:  
    points_table=[]
    nations=[]
    values=[]                                                 
    def __init__(self,filename1,filename2):
        '''Reading the contents of the CSV files.'''
        f=open(filename1,"r")
        #aranging the data of file in list seperating through ','
        for a in f.readlines():
            self.values.append(a.split(','))           
        f.close()

        file=open(filename2,"r")
        #arranging the list of name of countries
        for b in file.readlines():          
            self.nations.append(b[:-1])
        f.close()
    def points(self):
        '''Calculating the win, loss, draw, diff, for, aganist of the teams through CSV file.'''
        for country in self.nations:                                  #takes names of countries
            w=l=d=match_played=forr=against=diff=points=0             #assigning the value to 0
            for detail in self.values:
                if country in detail:                                 #checking if country is inside the detail
                    match_played+=1            
                    #the score an be in index 1 or 3 so adding 1 after country insex to take out score
                    homegoal_value=detail.index(country)+1            #adding 1 to current position to take index value
                    # using 4-score concept to take the opponent goal vale which is either index 1 or 3
                    awaygoal_value=4-homegoal_value                   #storing opponent team index value
                    
                    #assigining values
                    country_team=int(detail[homegoal_value])          #string the goal of country side team
                    opponent_team=int(detail[awaygoal_value])         #storing the goal of opponent team

                    #comparing scores 
                    if country_team<opponent_team:                    #chcking the condition for match losing
                        l+=1
                        forr+=country_team
                        against+=opponent_team 
                    elif country_team>opponent_team:                  #checking the condition for match winning
                        w+=1
                        forr+=country_team
                        against+=opponent_team
                        points+=3 
                    else:                                             #if both condition is not correct
                        d+=1
                        forr+=country_team
                        against+=opponent_team
                        points+=1
                    diff=forr-against                                 #finding the difference through for and aganist
            self.points_table.append([country,match_played,w,d,l,forr,against,diff,points])      #storing the values in a list
  
    def sorting(self):
        '''Sorting the order in points table with respect to the goal difference.'''
        for i in range(len(self.points_table)):                          #looping                  
            for j in range(i):                                           #nested loop
                if self.points_table[i][-2]>self.points_table[j][-2]:    #checking the diff to arrange in descending order
                #Replacing in a format a=b,b=c,c=a format   
                    temp=self.points_table[i]                            
                    self.points_table[i]=self.points_table[j]            
                    self.points_table[j]=temp

    def output(self):
        '''Displaying points table in a proper format through all the calculations.'''
        print("\t P    W    D    L     F      A    Diff   Points")
        for manage in self.points_table: 
            print(f"{str(manage[0]).ljust(9)}{str(manage[1]).ljust(5)}{str(manage[2]).ljust(5)}{str(manage[3]).ljust(5)}{str(manage[4]).ljust(5)}{str(manage[5]).ljust(7)}"
            f"{str(manage[6]).ljust(6)}{str(manage[7]).ljust(9)}{str(manage[8]).ljust(7)}")

if __name__=="__main__":
    values=sys.argv[1:]
    if len(values)==0:                                                  
        teams=league("results.csv","teams.csv")
    else:
        print("\n")
        if values[0]=="Euro 2020 Group D":                                #checking for command line condition
            print(values[0])
            print("="*len(values[0]))
            teams=league("result2.csv", "teams2.csv")   
        else:
            print(values[0])
            print("="*len(values[0]))
            teams=league("results.csv","teams.csv")         
teams.points()
teams.sorting()
teams.output()