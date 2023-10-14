import random
import copy  
import sys
import os
import pathlib

test = os.getcwd()
print(test+"/Jolgerat/stats.py")
# The creatures (0:names,1:strength,2:health,3:class)
knight = ["Knight",6,12,"creature"]
demon = ["Demon",15,10,"creature"]
prince = ["Prince",7,7,"creature"]
crow = ["Crow",5,3,"creature"]
skeleton = ["Skeleton",10,5,"creature"]
# The spells (0:names,1:placeholder,2:placeholder,3:class)
joker = ["Joker","","","spell"]
sacrifice_shield = ["Sacrifice Shield","","","spell"]
execution = ["Execution","","","spell"]
smith = ["Smith","","","spell"]
trap = ["Trap","","","spell"]

# The decks
deckA = [
    knight, knight, knight, knight, demon, demon, crow, crow, crow, crow, crow, prince, prince, prince, prince, skeleton, skeleton, skeleton, skeleton,
    joker, sacrifice_shield, sacrifice_shield, sacrifice_shield, execution, execution, execution, execution, smith, smith, smith, smith, smith,
    trap, trap
    ]
deckB = copy.deepcopy(deckA)
cardA1 = "default"
cardA2 = "default"
cardA3 = "default"
handA = "default"

# This changes the cards from player A
def drawA():
    global cardA1
    global cardA2
    global cardA3
    global deckA
    global handA

    if cardA1 == "default":
        cardA1 = copy.deepcopy(random.choice(deckA))
        deckA.remove(cardA1)

    if cardA2 == "default":
        cardA2 = copy.deepcopy(random.choice(deckA))
        deckA.remove(cardA2)

    if cardA3 == "default":
        cardA3 = copy.deepcopy(random.choice(deckA))
        deckA.remove(cardA3)

    handA = [cardA1, cardA2, cardA3]

    return cardA1, cardA2, cardA3, deckA, handA


# Hand B
cardB1 = "default"
cardB2 = "default"
cardB3 = "default"
handB = "default"

# This changes the cards from player B
def drawB():
    global cardB1
    global cardB2
    global cardB3
    global deckB
    global handB

    if cardB1 == "default":
        cardB1 = copy.deepcopy(random.choice(deckB))
        deckB.remove(cardB1)

    if cardB2 == "default":
        cardB2 = copy.deepcopy(random.choice(deckB))
        deckB.remove(cardB2)

    if cardB3 == "default":
        cardB3 = copy.deepcopy(random.choice(deckB))
        deckB.remove(cardB3)

    handB = [cardB1, cardB2, cardB3]

    return cardB1, cardB2, cardB3, deckB, handB


# The dice
AdStrengthA = 0
AdStrengthB = 0

def roll():
    global AdStrengthA
    global AdStrengthB

    AdStrengthA = random.randint(1,6)
    AdStrengthB = random.randint(1,6)
    print("Your Additional strength:",AdStrengthA)
    print("Your enemys Additional strength",AdStrengthB)
    
    return AdStrengthA, AdStrengthB

cardA = "default"
cardB = "default"
choice = "default"
fieldA = "default"
fieldB = "default"
spellA = "default"
spellB = "default" # right now bots can't use spells so this variable is useless
sac_decision = []

# The functions for the spells
def spell_smith():
    global fieldA
    fieldA[1] += 5
    return fieldA
def spell_joker():
    global fieldA
    global fieldB
    fieldA = "default"
    fieldB = "default"
    return fieldA,fieldB
def spell_sacrifice_shield1(): # To do
    global playerHealthA
    global pHA
    global sac_decision
    global handA
    global damage
    if playerHealthA != pHA:
        pHA = copy.copy(playerHealthA)
    return playerHealthA,pHA
def spell_sacrifice_shield2():
    global playerHealthA
    global pHA
    global damage
    global handA
    if cardA1 == sacrifice_shield:
        cardA1 = "default"
        drawA()
    elif cardA2 == sacrifice_shield:
        cardA2 = "default"
        drawA()
    elif cardA3 == sacrifice_shield:
        cardA3 = "default"
        drawA()
    if playerHealthA < pHA:
        choice = input("You are about to take ",damage," damage! Do you want to play a Sacrifice Shield?[y/n] ")
        if choice == "y":
            if cardA1[3] == "creature"or cardA1[3] == "creatureE":
                sac_decision.append("[1]",cardA1[0:3])
            elif cardA1[3] != "creature"or cardA1[3] == "creatureE":
                sac_decision.append("[/]","")
            if cardA2[3] == "creature"or cardA1[3] == "creatureE":
                sac_decision.append("[2]",cardA2[0:3])
            elif cardA2[3] != "creature"or cardA1[3] == "creatureE":
                sac_decision.append("[/]","")
            if cardA3[3] == "creature"or cardA1[3] == "creatureE":
                sac_decision.append("[3]",cardA3[0:3])
            elif cardA3[3] != "creature"or cardA1[3] == "creatureE":
                sac_decision.append("[/]","")
            print(sac_decision)
            sacrifice = input("(",sac_decision[0],sac_decision[2],sac_decision[4],")")
            if sacrifice == "1" and sac_decision[0] != "[/]":
                damage -= cardA1
                damage2 = copy.copy(damage) #to do
                if damage <= 0:
                    damage = 0
                print("Your",sac_decision,)
            elif sac_decision[0] == "[/]":
                print("You can't sacrifice that card")
    return damage, pHA, playerHealthA, handA


def spell_execution():
    global fieldA
    global handA
    global handB
    fieldA = "default"
    cardSelection(handA, handB)
    return fieldA,handA,fieldB
def spell_trap():
    global fieldB
    global trap
    global spellA

    if spellA == "default":
        spellA = trap

    if fieldB != "default":
        fieldBempty = False
    elif fieldB == "default":
        fieldBempty = True
    elif spellA != "default":
        print("You can't play a Trap now")

    if fieldBempty:
        if fieldB == "default": 
            fieldA[1] -= 5
            fieldA[2] -= 5
            spellA = "default"

    return fieldA, fieldB, spellA

# def spellcasting #this will remove spells from the hand and do other things like that

# This is where the cards get selected
def cardSelection(handA, handB):
    global cardA
    global cardB  
    global choice
    global fieldA
    global fieldB

    if fieldB == "default":
        cardB = copy.deepcopy(random.choice(handB))
        fieldB = cardB
    if fieldA == "default":
        print("[1]", cardA1[0], cardA1[1], cardA1[2], "[2]", cardA2[0], cardA2[1], cardA2[2], "[3]", cardA3[0], cardA3[1], cardA3[2])
        while choice != "1" or "2" or "3":
            choice = input(str("Select a card (1/2/3): "))
            if choice == "1":
                cardA = copy.deepcopy(handA[0])
                fieldA = cardA
                choice = "0"
                break
            elif choice == "2":
                cardA = copy.deepcopy(handA[1])
                choice = "0"
                fieldA = cardA
                break
            elif choice == "3":
                cardA = copy.deepcopy(handA[2])
                fieldA = cardA
                choice = "0"
                break
            else:
                print("please select a card")
    return cardA, choice, cardB, fieldA, fieldB


def removeFromHand():
    global cardA
    global cardB
    global cardA1
    global cardA2
    global cardA3
    global deckA
    global handA
    global cardB1
    global cardB2
    global cardB3
    global deckB
    global handB

    if cardA == cardA1:
        cardA1 = "default"
    elif cardA == cardA2:
        cardA2 = "default"
    elif cardA == cardA3:
        cardA3 = "default"
    elif cardB == cardB1:
        cardB1 = "default"
    elif cardB == cardB2:
        cardB2 = "default"
    elif cardB == cardB3:
        cardB3 = "default"
    return cardA1,cardA2,cardA3,cardB1,cardB2,cardB3,cardA,cardB,handB,handA,deckA,deckB

strenghA=0
strengthB=0
damage=0
playerHealthA = 20
playerHealthB = 20
pHA = 0
s1=0
s2=0
s3=0
s4=0

# this function does all the mathmatical stuff for the fights between the creatures ant it lowers the player health if it should get lower
def fight():
    global fieldA
    global fieldB
    global strenghA
    global strenghB
    global damage
    global playerHealthA
    global playerHealthB
    global s1
    global s2
    global s3
    global s4
    print(input("enter to start fight"))
    roll()
    s1=copy.copy(fieldA[1])
    s2=copy.copy(fieldA[1])
    s3=copy.copy(fieldB[1])
    s4=copy.copy(fieldB[1])
    strenghA = fieldA[1] + int(AdStrengthA)
    strenghB = fieldB[1] + int(AdStrengthB)
    if strenghA > strenghB:
        damage=strenghA - strenghB
        if damage > fieldB[2]:
            damage = damage - fieldB[2]
            fieldB[2]=0
            playerHealthB = playerHealthB - damage
            print("Your creature wins and inflicts",damage,"damage to your enemy")
            print("Your enemy has",playerHealthB,"left")
        else:
            fieldB[2] = fieldB[2] - damage
            print("Your creature wins and inflicts",damage,"damage")
    elif strenghA < strenghB:
        damage=strenghB - strenghA
        if damage > fieldA[2]:
            damage = damage - fieldA[2]
            fieldA[2]=0
            playerHealthA = playerHealthA - damage
            print("Your enemys creature wins and inflicts",damage,"damage to you")
            print("You have",playerHealthA," health left")
        else:
            fieldA[2] = fieldA[2]- damage
            print("Your enemys creature wins and inflicts",damage,"damage")
    elif strenghA == strenghB:
        print("Draw")

    fieldA[1] = s2 - s3
    fieldB[1] = s4 - s1
    s1=copy.copy(fieldA[1])
    s2=copy.copy(fieldA[1])
    s3=copy.copy(fieldB[1])
    s4=copy.copy(fieldB[1])

    if fieldA[1] < 1:
        fieldA[1]= 1
    if fieldB[1] < 1:
        fieldB[1]= 1

    return fieldA,fieldB,damage,playerHealthA,playerHealthB

# this function checks if a creature or the player is dead, and it tracks the looses and the wins
def check1():
    global playerHealthA
    global playerHealthB
    if playerHealthA <= 0:
        playerHealthA = 0
        print("You lost!")
       # with open("Stats.py", "a") as f:
        #    f.write("You: {}\nEnemy: {}\n".format(player_score, ai_score))
    elif playerHealthB <= 0:
        playerHealthB
        print("You win!")
    
def check2():
    global fieldA
    global fieldB
    if fieldA[2] <= 0:
        print("Your",fieldA[0] + "  is dead")
        fieldA= "default"
    elif fieldB[2] <= 0:
        print("Your enemys",fieldB[0] + " is dead")
        fieldB= "default"
    return fieldA,fieldB

# The preparation of the Stats.py file
#if os.path.getsize("stats.py") == 0:
#    with open("stats.py", "w") as f:
#        f.write("Wins = 0\n")
#        f.write("Looses = 0\n")


# the menu
print("WELCOME TO JOLGERAT")
print(" ")
print("[1] Play")
print("[2] Tutorial")
print("[3] Stats")
print("[4] Credits")
print("[5] Exit")
firstChoice = input("1/2/3/4/5 ")
while firstChoice == "1"or"2"or"3"or"4"or"5":
    if firstChoice == "1": # play
        # The core
        while playerHealthA > 0 and playerHealthB > 0:
            drawA() 
            drawB()
            cardSelection(handA,handB)
            removeFromHand()
            print("You:",fieldA[0],"S:",fieldA[1],"H:",fieldA[2])
            print("Enemy:",fieldB[0],"S:",fieldB[1],"H:",fieldB[2])
            fight()
            check2()
            check1()
        input("enter to go back to main menu ")
        print(" ")
        print("[1] Play")
        print("[2] Tutorial")
        print("[3] Stats")
        print("[4] Credits")
        print("[5] Exit")
        firstChoice = input("1/2/3/4/5 ")
    elif firstChoice == "2": # Turtorial ; Update turtorial
        print("Each player draws three cards, then chooses one of the cards to play in the center.")
        print("As soon as he plays a card, he draws a new one.")
        print("Each card is a creature and each creature has a base strength and health.")
        print("At the beginning of a combat sequence, each player rolls a dice, and the value rolled (additional strength) is added to the base strength for that combat sequence.")
        print("The creature with the higher combat strength (base strength + additional strength) wins the combat")
        print("and the creature that lost gets the combat strength it could not absorb with its own combat strength subtracted from its health.")
        print("If a creature cannot absorb the combat strength with its own health, it dies and the excess combat strength is subtracted from the health of the player whose creature died.")
        print("At the end of each battle, each creature loses base strength equal to the base strength of the other creature.")
        print("Each player has 20 health, if the health of a player drops to 0, he has lost.")
        input("enter to go back to main menu ")
        print(" ")
        print("[1] Play")
        print("[2] Tutorial")
        print("[3] Stats")
        print("[4] Credits")
        print("[5] Exit")
        firstChoice = input("1/2/3/4/5 ")
    elif firstChoice == "3": # Stats 
        print("This feature is not done yet. Come back another time :)")
        #with open("stats.py", "r") as f:
       #      print(f.read())
        input("enter to go back to main menu ")
        print(" ")
        print("[1] Play")
        print("[2] Tutorial")
        print("[3] Stats")
        print("[4] Credits")
        print("[5] Exit")
        firstChoice = input("1/2/3/4/5 ")
    elif firstChoice == "4": # Credits
        print("Eleseus")
        print("DVillablanca")
        print("Chat GPT")
        input("enter to go back to main menu ")
        print(" ")
        print("[1] Play")
        print("[2] Tutorial")
        print("[3] Stats")
        print("[4] Credits")
        print("[5] Exit")
        firstChoice = input("1/2/3/4/5 ")
    elif firstChoice == "5": # Exit 
        sys.exit()

# I used this codeblock to test everything
#drawA()
#drawB()
#cardSelection(handA,handB)
#print("Your card: ",fieldA[0],"S:",fieldA[1],"H:",fieldA[3])
#print("Opponents card",fieldB[0],"S:",fieldB[2],"H:",fieldB[3])
#removeFromHand()
#fight(fieldA,fieldB)
#drawA()
#drawB()
#cardSelection(handA,handB)
#print("Your card: ",fieldA[0],"S:",fieldA[1],"H:",fieldA[3])
#print("Opponents card",fieldB[0],"S:",fieldB[2],"H:",fieldB[3])