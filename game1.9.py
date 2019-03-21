#Omar De La Torre
#3/16/19

#Omar's Adventure Game

import random



print("Starting Omar's Adventure Game")

playerName = input("Enter player name to start: ")

print("The year is 2177, humans have finished draining Earth of its resources and are onto taking the life of other planets. Mars and Venus have been colonozed, but are not the utopias everyone expected. Instead, they are lawless, endless, strips of cities and smaller civilization.")

print("However, some people still seek to better these other planets. Not all of these people share common morals in the journey to improvement." ,playerName,"is currently in search of something that could contribute to a rapid change in the solar system. Whether the change is good or bad, is up to whoever is in possesion...")
print("You land into a dusty town in the middle of Venus to continue your journey in search of that something. You take time to explore the town.")

currency=3516 #currency not fully implemented


#need to add else statements for other/invalid inputs 

def diceThugs():                                    #this is the thugs gambling function
    roll=int(input("Roll? Yes(1)- No(2): "))
    if roll==1:
        playerRoll=random.randint(1,12)         #generate two random numbers from 1-12 and compare them
        thugRoll=random.randint(1,12)
        if playerRoll>thugRoll:
            print("You rolled a" ,playerRoll," I rolled a" ,thugRoll," ugh you win.")
            diceThugs()
        elif playerRoll==thugRoll:
            print("Mmmm tie..")                         #after result you get chance to roll again or go back
            diceThugs()
        elif playerRoll<thugRoll:
            print("You rolled a" ,playerRoll," I rolled a" ,thugRoll," haha ya lose!")
            diceThugs()     
    elif roll==2:   
        actionChapter1()
    
    


def actionChapter3():
    action3=int(input("Choose what to investigate: Small Shed(1) - Old Car(2) - Main Building(3):  ")) #chapter 3 and forward will begin to get more linear

    if action3==1:
        print("You find a dying survivor who tells you that the group of men passed through here on their way to the little town. He doesn't look like he's going to make it. He asks you to leave him in peace.")
        actionChapter3()
    elif action3==2:
        print("You search around the old car looking for supplies and seeing if it will run. No luck with the car, but you find a small amount of loot.") #add loot if invetory implemented
        actionChapter3() 
    elif action3==3:
        print("As you are heading towards the main bulding, you hear the sound of vehicles growing louder and louder and you realize what's going on. Some of the men must have tracked you and are here to tie up loose ends...")
        print("Two cars pull up and 3 men get out of each car. This time you will be forced to fight.") #add fight/combat function
        print("After the battle you gather supplies from the defeated enemies and recognize a crest on one of the men's rings. You know it belongs to a cult located not too far. If anyone has information on what you're looking for, it must be them.")
        print("Once you regained your bearings you accurately located the hide out. It is an old warehouse with little attraction at the surface, but you see a door and hear some activity behind it...")
        print("To be continued....")
        #actionChapter4() 

def actionChapter2():
    action2=int(input("Choose an action: Peek outdoors(1) - Attempt to fight(2) - Look to aid townsfolk(3) - Run away(4):  "))
    if action2==1:
        print("You peek out the window. Your view is obstructed by wooden panels outside of the window. However, you are able to catch a glimpse of 2 dark cars and a few men in suits. How original.")
        actionChapter2()
    elif action2==2:
        print("You run outside and see...")  #add fight/combat function
        print("After all that you are able to slip out the back end of town. You still have no leads, but you are certain that the mysterious group of men have ties to all this.")
        print("You continued on foot East of the little town. No sign of civilization for miles. As the sun rises you can see a structure in the distance. When you get to it, you see that it is some sort of an abonadoned gas station. Everything is very still. As if the building and everything around it was not real but instead you were looking at a giant image. It's the only thing around so...")        
        actionChapter3()
                                            #make it so your fight is succesful if you bought a gun if not you are injured and you run away if invetory is implemented
        
    elif action2==3:
        print("You search around undetected and see the Old Cat Lady, Tired Mechanic, and one of the inn patrons struggling to find safety.")
        aid1=int(input("Choose who to aid: Old Cat Lady(1) - Tired Mechanic(2) - Inn Patron(3):  ")) #gain currency or item of implemented depending on who is aided
                                                                                                    #after you make a decision you go to chapter 3
        if aid1==1:
            print("Thanks stranger! Me and my cat 'Dog' will be forever grateful.")
            print("After all that you are able to slip out the back end of town. You still have no leads, but you are certain that the mysterious group of men have ties to all this.")
            print("You continued on foot East of the little town. No sign of civilization for miles. As the sun rises you can see a structure in the distance. When you get to it, you see that it is some sort of an abonadoned gas station. Everything is very still. As if the building and everything around it was not real but instead you were looking at a giant image. It's the only thing around so...")        
            actionChapter3()
        elif aid1==2:
            print("I am forever in your debt.")
            print("After all that you are able to slip out the back end of town. You still have no leads, but you are certain that the mysterious group of men have ties to all this.")
            print("You continued on foot East of the little town. No sign of civilization for miles. As the sun rises you can see a structure in the distance. When you get to it, you see that it is some sort of an abonadoned gas station. Everything is very still. As if the building and everything around it was not real but instead you were looking at a giant image. It's the only thing around so...")        
            actionChapter3()
        elif aid1==3:
            print("Thanks a ton. Here's a cold one for the road.")
            print("After all that you are able to slip out the back end of town. You still have no leads, but you are certain that the mysterious group of men have ties to all this.")
            print("You continued on foot East of the little town. No sign of civilization for miles. As the sun rises you can see a structure in the distance. When you get to it, you see that it is some sort of an abonadoned gas station. Everything is very still. As if the building and everything around it was not real but instead you were looking at a giant image. It's the only thing around so...")        
            actionChapter3()

    elif action2==4:
        print("After all that you are able to slip out the back end of town. You still have no leads, but you are certain that the mysterious group of men have ties to all this.")
        print("You continued on foot East of the little town. No sign of civilization for miles. As the sun rises you can see a structure in the distance. When you get to it, you see that it is some sort of an abonadoned gas station. Everything is very still. As if the building and everything around it was not real but instead you were looking at a giant image. It's the only thing around so...")        
        actionChapter3()



def actionChapter1():
    currency=3516
    action1 = int(input("Choose an action: Shop(1) - Go to inn(2) - Speak to locals(3) :  "))
    if action1==1:
        print("How are ya? Whadya care to buy? (You currently have" ,currency, "credits in your bag)")
        buy1 = int(input("Choose an item: Pistol: 3500 credits(1), Nourishment: 800 credits(2), Nothing: Go back(3) : ")) #shop module
        if buy1==1:
            print("Ooo whad'ya up to buying somethin' like that? Anyways.. have a good one!")
            #currency-=3500
            #print("Currency:" ,currency) #need to work on currency. make it so only 1 item is purchaseable or cannot repeat same actions*
            actionChapter1()
        elif buy1==2:
            print("Snacks for the night eh? Take care now!")
            actionChapter1()
        elif buy1==3:
            print("Hmph. Bye bye now.")
            actionChapter1()

    elif action1==2:
        print("You step into the inn, and you are greeted by a few shifty and tired looks. You notice little activity except for a handful of patrons and a lack luster boxing circle.")
        inn1=int(input("Choose an action: Box(1) - Converse(2) - Get a room and sleep(3) :  "))

        if inn1==1:
            print("Oy! Think you got what it takes? Let's see it then!") #might change to something so you can do a game involving simple number inputs
            actionChapter1()
        if inn1==2:
            ques=int(input("How would you like to approach? : Politely (1) - Insensible(2) - Cautiously(3) : "))            #depending on how you approach you will get varied responses
            if ques==1:
                print("You're not getting anywhere round these parts with a talk like that. Shove off.")
                actionChapter1()
            elif ques==2:
                print("Not much to do around this piss poor town but drink and box. Everyone is shifty about tonight though...")
                actionChapter1()
            elif ques==3:
                print("Why so nervous boyo? Don't worry tonight should go by fine if you keep down.")
                actionChapter1()
        elif inn1==3:
            print("Only got one room without mold. You can stay for free if you leave by sunrise..")                #when sleep in a room moves on to chapter 2
            print("It is is early morning and still dark out. You hear thousands of muffled tiny thuds. As you're half asleep you realize that it is storming in the little town and there is massive claps of thunder. As you fully wake you notice some of the thunder sounds closer and different than others.")
            print("You suddenly hear glass break downstairs and realize some of the thunder are gun shots. You scramble quickly out of bed and...")
            actionChapter2()
                      
    elif action1==3:
        print("You walk around town trying to find someone approachable to get some general information and maybe a lead for your search..") #all give some hints about an event happening tonight
        talk=int(input("Choose who to talk to: Thugs Gambling(1) - Old Cat Lady(2) - Tired Mechanic(3): "))
        if talk==1:
            print("No talking roll...")
            print("Here's how this goes. You roll a higher number than me you win, you roll less you lose..")#try rand game
            diceThugs()           
        elif talk==2:
            print("Fluffles seemed too generic so my cat's name is 'Dog'! She seems scared about tonight.")
            actionChapter1()
        elif talk==3:
            print("I'm closed for the day come back tomorrow... if I'm lucky I'll open up tomorrow..")
            actionChapter1()

            

actionChapter1()

    

    
