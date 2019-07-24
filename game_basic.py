# name: Paige Sanford
# date: 2019-07-13
# description: Text-based medieval adventure game

import random
import time

def displayIntro():
    print("\nHello, Sir Knight! Join us on a quest to a castle.")
    time.sleep(3)
    print("\nWe hear tell of great treasure in a castle not too far from here.")
    time.sleep(3)
    print("\nYou're interest is peaked, so you consider joining this curious band of mis-fits.")
    time.sleep(3)
    
    print('\nPath 1: Say "No Thanks" \n  OR  \n  Path 2:  Ride along with them on your noble steed?')
    time.sleep(3)
    print('...')

def chooseOption():
    option = ""
    while option != "1" and option != "2" and option != "q": #input validation
        option = input("Choose a path: (1 or 2): \nPrithee, Maketh thou choice wisely! " )
        
        if option != "1" and option != "2" and option != "q":
            print("Your brain is as dry as the remainder biscuit after voyage.")
                        #Shakespeare – As You Like It (Act 2, Scene 7))
            print("Thou entered vile input!")

    return option

def checkOption(chosenOption):
    print(chosenOption)
    if chosenOption == "1":
        print("Verily, Thou hast chosen.")
        time.sleep(2)
        print("\nThou art wise, but brave be thou not!")
        time.sleep(2)
    elif chosenOption == "q":
        pass
    else:
        print("Verily, Thou hast chosen.")
        time.sleep(2)
        print("\nA storm is coming, but the Castle is in sight, so ye travel on.")
        time.sleep(2)
        print("\nA great ogre cometh out of the woods chasing thee hastily.")
        time.sleep(2)
        correctOption = random.randint(1, 2)

        if chosenOption == str(correctOption):
            print("\nYe draw yon bow, and shootest the ogre dead with yay one shot.")
            time.sleep(3)
            print("\nThou art applauded by the group for thine great shot, and are thus appointed leader.")
            print("\nYe have chosen wisely!")
        else:
            print("\nThine horse is frightened by the ogre and cast thee off.")
            time.sleep(3)
            print("\nThou sense great pain, as soon as ye fall to the ground.")
            time.sleep(3)
            print("\nThe ogre has slammed a battle ax deep into thine back, nearly splitting ye asunder.")
            time.sleep(3)
            print("\ntaking thine last breath, thou wonderest why didn't thou say",'"No Thanks!"')
        
def gameflow():
    playAgain = "Yes"
    while playAgain == "Yes" or playAgain == "y":
        displayIntro()
        choice = chooseOption()
        checkOption(choice) #choice is equal to "1" or "2"
        playAgain = input("Doth ye want to play again? (Yes or y to go again.) ")
    
        if playAgain == "No" or playAgain =="n":
            print("Thine quest hast ended!  Fare Thee Well!!")

    

#display main menu
print("---Welcome to LONG-KNIGHTS-AND-CASTLE-DAZE Game!---")
print()
print("A medieval text adventure game.")
print()
print("Yea, verily here we goeth!")
time.sleep(2)
   
gameflow()
