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
sacrifice_shield = ["Sacrifice Shield","","","spellspecial"]
execution = ["Execution","","","spell"]
smith = ["Smith","","","spell"]
trap = ["Trap","","","spell"]

# The decks
deckA = [
    knight, knight, knight, knight, demon, demon, crow, crow, crow, crow, crow, prince, prince, prince, prince, skeleton, skeleton, skeleton, skeleton,
    joker, sacrifice_shield, sacrifice_shield, sacrifice_shield, execution, execution, execution, smith, smith, smith, trap, trap
    ]
deckB = copy.deepcopy(deckA)
deckB = [card for card in deckB if card[3] != "spell" and card[3] != "spellspecial"]
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
    if cardA1[3] != "creature" and cardA1[3] != "creatureE" and cardA2[3] != "creature" and cardA2[3] != "creatureE" and cardA3[3] != "creature" and cardA3[3] != "creatureE":
        print("You have no creature, select a card to discard")
        print("[1]",cardA1[0],"[2]",cardA2[0],"[3]",cardA3[0])
        discard_choice = input("(1/2/3) ")
        if discard_choice == "1":
            cardA1 = "default"
            drawA()
        elif discard_choice == "2":
            cardA2 = "default"
            drawA()
        elif discard_choice == "3":
            cardA3 = "default"
            drawA()
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
creatureA = "default"
creatureB = "default"
spellA = "default"
spellB = "default" # right now bots can't use spells so this variable is useless
sac_decision = []
text = "default"
creature_selection = []
spell_selection =  []
spell_choice = "default"

# The functions for the spells
def spell_smith():
    global creatureA
    creatureA[1] += 5
    print(f"Your {creatureA[0]} now has {creatureA[1]} strength")
    return creatureA
def spell_joker():
    global creatureA
    global creatureB
    creatureA = "default"
    creatureB = "default"
    cardSelection(handA,handB)
    print("The field is empty now")
    return creatureA,creatureB
def spell_sacrifice_shield1(): 
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
    global cardA1
    global cardA2
    global cardA3
    global damageaverted
    global text
    if playerHealthA < pHA and sacrifice_shield in handA:
        choice = input("You are about to take " + str(damage) + " damage! Do you want to use a Sacrifice Shield?[y/n] ")
        if choice == "y":
            if cardA1 == sacrifice_shield:
                cardA1 = "default"
                drawA()
            elif cardA2 == sacrifice_shield:
                cardA2 = "default"
                drawA()
            elif cardA3 == sacrifice_shield:
                cardA3 = "default"
                drawA()

            sac_decision = []

            if cardA1[3] == "creature" or cardA1[3] == "creatureE":
                sac_decision.append("[1]")
                sac_decision.append(cardA1[0:3])
            elif cardA1[3] != "creature" or cardA1[3] != "creatureE":
                sac_decision.append("[/]")
                sac_decision.append("")

            if cardA2[3] == "creature" or cardA2[3] == "creatureE":
                sac_decision.append("[2]")
                sac_decision.append(cardA2[0:3])
            elif cardA2[3] != "creature" or cardA2[3] != "creatureE":
                sac_decision.append("[/]")
                sac_decision.append("")

            if cardA3[3] == "creature" or cardA3[3] == "creatureE":
                sac_decision.append("[3]")
                sac_decision.append(cardA3[0:3])
            elif cardA3[3] != "creature" or cardA3[3] != "creatureE":
                sac_decision.append("[/]")
                sac_decision.append("")

            print(sac_decision[0], sac_decision[1], sac_decision[2], sac_decision[3], sac_decision[4], sac_decision[5])
            sacrifice = input("(" + sac_decision[0] + sac_decision[2] + sac_decision[4] + ") ")
            
            while sacrifice != "1" or "2" or "3":
                if sacrifice == "1" and sac_decision[0] != "[/]":
                    damage2 = copy.copy(damage)
                    damage -= cardA1[2]
                    if damage < 0:
                        damage = 0
                    text = ("Your ", sac_decision[1], " saved you from ", str(damage2), " damage, you only lose " + str(damage) + " health")
                    print(text)
                    damageaverted = damage2 - damage
                    break
                elif sacrifice == "2" and sac_decision[2] == "[/]":
                    print("You can't sacrifice that card")
                elif sacrifice == "2" and sac_decision[2] != "[/]":
                    damage2 = copy.copy(damage)
                    damage = damage - cardA2[2]
                    if damage < 0:
                        damage = 0
                    if damage2 < 0:
                        damage2 = 0
                    text = ("Your ", sac_decision[3], " saved you from ", str(damage2), " damage, you only lose " + str(damage) + " health")
                    print(text)
                    damageaverted = damage2 - damage
                    break
                elif sacrifice == "3" and sac_decision[4] != "[/]":
                    damage2 = copy.copy(damage)
                    damage -= cardA3[2]
                    if damage < 0:
                        damage = 0
                    if damage2 < 0:
                        damage2 = 0
                    text = ("Your ", sac_decision[5], " saved you from ", str(damage2), " damage, you only lose " + str(damage) + " health")
                    print(text)
                    damageaverted = damage2 - damage
                    break
                elif sacrifice == "3" and sac_decision[4] == "[/]":
                    print("You can't sacrifice that card")
                else:
                    print("Please select a creature to sacrifice")
    sac_decision = []
    return damage, pHA, playerHealthA, handA, cardA1, cardA2, cardA3, damageaverted, text
def spell_execution():
    global creatureA
    global handA
    global handB
    print(f"Your {creatureA[0]} was executed")
    creatureA = "default"
    cardSelection(handA, handB)
    return creatureA,handA,creatureB
def spell_trap():
    global creatureB
    global trap
    global spellA

    if creatureB != "default":
        creatureB[1] -= 5
        creatureB[2] -= 5
        if creatureB[2] > 0:
            print(f"Your enemys {creatureB[0]} has {creatureB[1]} strength and {creatureB[2]} health left")
        elif creatureB[2] <= 0:
            print(f"Your enemys {creatureB[0]} is dead because of your Trap")
    if creatureB == "default":
        print("You can't play a trap now")

    return creatureB, spellA

# This function checks wich spell has to be executed and executes it
def spellcasting(card):
    global creatureA
    global creatureB
    global spellA
    global spellB
    global cardA1
    global cardA2
    global cardA3
    if card[0] == "Smith":
        spell_smith()
    elif card[0] == "Joker":
        spell_joker()
    elif card[0] == "Execution":
        spell_execution()
    elif card[0] == "Trap":
        spell_trap()
    return card

# This is where the cards get selected
def cardSelection(handA, handB):
    global cardA
    global cardB  
    global choice
    global spell_choice
    global creatureA
    global creatureB
    global spellA
    global spellB
    global cardA1
    global cardA2
    global cardA3
    global creature_selection
    global spell_selection

    if creatureB == "default":
        cardB = copy.deepcopy(random.choice(handB))
        creatureB = cardB
    if cardA1[3] == "creature" or cardA1 == "creatureE":
        creature_selection.append("([1]")
        creature_selection.append(cardA1[0])
        creature_selection.append(cardA1[1])
        creature_selection.append(cardA1[2])
        creature_selection.append(")")
    elif cardA1[3] != "creature" or cardA1 != "creatureE":
        creature_selection.append("([/]")
        creature_selection.append(cardA1[0])
        creature_selection.append(")")
    if cardA2[3] == "creature" or cardA2 == "creatureE":
        creature_selection.append("([2]")
        creature_selection.append(cardA2[0])
        creature_selection.append(cardA2[1])
        creature_selection.append(cardA2[2])
        creature_selection.append(")")
    elif cardA2[3] != "creature" or cardA2 != "creatureE":
        creature_selection.append("([/]")
        creature_selection.append(cardA2[0])
        creature_selection.append(")")
    if cardA3[3] == "creature" or cardA3 == "creatureE":
        creature_selection.append("([3]")
        creature_selection.append(cardA3[0])
        creature_selection.append(cardA3[1])
        creature_selection.append(cardA3[2])
        creature_selection.append(")")
    elif cardA3[3] != "creature" or cardA3 != "creatureE":
        creature_selection.append("([/]")
        creature_selection.append(cardA3[0])
        creature_selection.append(")")
    if creatureA == "default":
        # field_selection = ("[1]", cardA1[0], cardA1[1], cardA1[2], "[2]",cardA2[0], cardA2[1], cardA2[2], "[3]", cardA3[0], cardA3[1], cardA3[2])
        print(creature_selection)
        while choice != "1" or "2" or "3":
            choice = input(str("Select a creature (1/2/3): "))
            if choice == "1" and cardA1[3] != "spell":
                cardA = copy.deepcopy(handA[0])
                creatureA = cardA
                choice = "0"
                break
            elif choice == "2" and cardA2[3] != "spell":
                cardA = copy.deepcopy(handA[1])
                choice = "0"
                creatureA = cardA
                break
            elif choice == "3" and cardA3[3] != "spell":
                cardA = copy.deepcopy(handA[2])
                creatureA = cardA
                choice = "0"
                break
            else:
                print("please select a creature")
    creature_selection = []
    return cardA, choice, cardB, creatureA, creatureB, creature_selection, spell_selection, spellA, spellB

# This function removes cards from the hands # to do
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
        drawA()
    elif cardA == cardA2:
        cardA2 = "default"
        drawA()
    elif cardA == cardA3:
        cardA3 = "default"
        drawA()
    elif cardB == cardB1:
        cardB1 = "default"
        drawB()
    elif cardB == cardB2:
        cardB2 = "default"
        drawB()
    elif cardB == cardB3:
        cardB3 = "default"
        drawB()
    
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
damageaverted = 0

# this function does all the mathmatical stuff for the fights between the creatures ant it lowers the player health if it should get lower
def fight():
    global creatureA
    global creatureB
    global strenghA
    global strenghB
    global damage
    global playerHealthA
    global playerHealthB
    global s1
    global s2
    global s3
    global s4
    global damageaverted
    global text
    global spell_choice
    global spellA
    global spellB
    global cardA1
    global cardA2
    global cardA3
    global spell_selection
    global cardA
    drawA()
    drawB()
    if spellA == "default":
        while creatureB[3] != "default": 
            if cardA1[3] == "spell":
                spell_selection.append("([1]")
                spell_selection.append(cardA1[0])
                spell_selection.append(")")
            elif cardA1[3] != "spell":
                spell_selection.append("([/]")
                spell_selection.append(cardA1[0])
                spell_selection.append(")")
            if cardA2[3] == "spell":
                spell_selection.append("([2]")
                spell_selection.append(cardA2[0])
                spell_selection.append(")")
            elif cardA2[3] != "spell":
                spell_selection.append("([/]")
                spell_selection.append(cardA2[0])
                spell_selection.append(")")
            if cardA3[3] == "spell":
                spell_selection.append("([3]")
                spell_selection.append(cardA3[0])
                spell_selection.append(")")
            elif cardA3[3] != "spell":
                spell_selection.append("([/]")
                spell_selection.append(cardA3[0])
                spell_selection.append(")")
            if cardA1[3] == "spell" or cardA2[3] == "spell" or cardA3[3] == "spell":
                print(spell_selection)
                spell_choice = input("Select a spell. Enter for no spell ")
                if spell_choice == "1" and cardA1[3] == "spell":
                    spellA = cardA1
                    spellcasting(cardA1)
                    cardA = spellA
                    removeFromHand()
                    spellA = "default"
                    break
                elif spell_choice == "2" and cardA2[3] == "spell":
                    spellA = cardA2
                    spellcasting(cardA2)
                    cardA = spellA
                    removeFromHand()
                    spellA = "default"
                    break
                elif spell_choice == "3" and cardA3[3] == "spell":
                    spellA = cardA3
                    spellcasting(cardA3)
                    cardA = spellA
                    removeFromHand()
                    spellA = "default"
                    break
                else:
                   break
            else:
                break
    print(input("enter to start fight"))
    roll()
    s1=copy.copy(creatureA[1])
    s2=copy.copy(creatureA[1])
    s3=copy.copy(creatureB[1])
    s4=copy.copy(creatureB[1])
    strenghA = creatureA[1] + int(AdStrengthA)
    strenghB = creatureB[1] + int(AdStrengthB)
    if strenghA > strenghB:
        damage=strenghA - strenghB
        if damage > creatureB[2]:
            damage = damage - creatureB[2]
            creatureB[2]=0
            playerHealthB = playerHealthB - damage
            print("Your creature wins and inflicts",damage,"damage to your enemy")
            print("Your enemy has",playerHealthB,"left")
        else:
            creatureB[2] = creatureB[2] - damage
            print("Your creature wins and inflicts",damage,"damage")
    elif strenghA < strenghB:
        damage=strenghB - strenghA
        if damage > creatureA[2]:
            damage = damage - creatureA[2]
            creatureA[2]=0
            spell_sacrifice_shield1()
            playerHealthA = playerHealthA - damage
            spell_sacrifice_shield2()
            playerHealthA = playerHealthA + damageaverted
            damageaverted = 0
            text = "default"
            print("Your enemys creature wins and inflicts",damage,"damage to you")
            print("You have",playerHealthA," health left")
        else:
            creatureA[2] = creatureA[2]- damage
            print("Your enemys creature wins and inflicts",damage,"damage")
    elif strenghA == strenghB:
        print("Draw")

    creatureA[1] = s2 - s3
    creatureB[1] = s4 - s1
    s1=copy.copy(creatureA[1])
    s2=copy.copy(creatureA[1])
    s3=copy.copy(creatureB[1])
    s4=copy.copy(creatureB[1])

    if creatureA[1] < 1:
        creatureA[1]= 1
    if creatureB[1] < 1:
        creatureB[1]= 1
    spell_selection = []
    return creatureA, creatureB, damage, playerHealthA, playerHealthB, damageaverted, spell_choice, spellA, spellB, cardA1, cardA2, cardA3 , spell_selection

# These functions check if a creature or the player is dead, and it tracks the looses and the wins
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
    global creatureA
    global creatureB
    if creatureA[2] <= 0:
        print("Your",creatureA[0] + "  is dead")
        creatureA= "default"
    elif creatureB[2] <= 0:
        print("Your enemys",creatureB[0] + " is dead")
        creatureB= "default"
    return creatureA,creatureB

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
            print("You:",creatureA[0],"S:",creatureA[1],"H:",creatureA[2])
            print("Enemy:",creatureB[0],"S:",creatureB[1],"H:",creatureB[2])
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
#print("Your card: ",fieldA[0],"S:",fieldA[1],"H:" fieldA[3])
#print("Opponents card",fieldB[0],"S:",fieldB[2],"H:",fieldB[3])
#removeFromHand()
#fight(fieldA,fieldB)
#drawA()
#drawB()
#cardSelection(handA,handB)
#print("Your card: ",fieldA[0],"S:",fieldA[1],"H:",fieldA[3])
#print("Opponents card",fieldB[0],"S:",fieldB[2],"H:",fieldB[3])