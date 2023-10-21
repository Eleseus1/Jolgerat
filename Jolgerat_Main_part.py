import random
import copy  
import sys

# To do:
# fix strength reduction AGAIN
# Effect creatures
# Deck editor
# Update turtorial

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
        discard_choice = input("(1|2|3) ")
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
    global spellA
    creatureA[1] += 5
    print(f"Your {creatureA[0]} now has {creatureA[1]} strength")
def spell_joker():
    global creatureA
    global creatureB
    creatureA = "default"
    creatureB = "default"
    print("The field is empty now")
    drawA()
    creatureSelection(handA,handB)
    strength_reduction()
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

            if cardA1[3] == "creature" or cardA1[3] == "creatureE":
                sac_decision1 =("[1]")
                sac_decision2 =(cardA1[0],cardA1[1],cardA1[2])
            elif cardA1[3] != "creature" or cardA1[3] != "creatureE":
                sac_decision1 =("[/]")
                sac_decision2 =("")
            if cardA2[3] == "creature" or cardA2[3] == "creatureE":
                sac_decision3 =("[2]")
                sac_decision4 =(cardA2[0],cardA2[1],cardA2[2])
            elif cardA2[3] != "creature" or cardA2[3] != "creatureE":
                sac_decision3 =("[/]")
                sac_decision4 =("")
            if cardA3[3] == "creature" or cardA3[3] == "creatureE":
                sac_decision5 =("[3]")
                sac_decision6 =(cardA3[0],cardA3[1],cardA3[2])
            elif cardA3[3] != "creature" or cardA3[3] != "creatureE":
                sac_decision5 =("[/]")
                sac_decision6 =("")
            print(sac_decision1, sac_decision2, sac_decision3, sac_decision4, sac_decision5, sac_decision6)
            sacrifice = input("(" + sac_decision1 + sac_decision3 + sac_decision5 + ") ")
            while sacrifice != "1" or "2" or "3":
                if sacrifice == "1" and sac_decision1 != "[/]":
                    damage2 = copy.copy(damage)
                    damage -= cardA1[2]
                    if damage < 0:
                        damage = 0
                    text = (f"Your {cardA1[0]} saved you from {damage2} damage, you only lose {damage} health")
                    print(text)
                    damageaverted = damage2 - damage
                    if damageaverted > damage2:
                        damageaverted = damage2
                    break
                elif sacrifice == "1" and sac_decision1 == "[/]":
                    print("You can't sacrifice that card")
                    break
                elif sacrifice == "2" and sac_decision3 != "[/]":
                    damage2 = copy.copy(damage)
                    damage = damage - cardA2[2]
                    if damage < 0:
                        damage = 0
                    text = (f"Your {cardA2[0]} saved you from {damage2} damage, you only lose {damage} health")
                    print(text)
                    damageaverted = damage2 - damage
                    if damageaverted > damage2:
                        damageaverted = damage2
                    break
                elif sacrifice == "2" and sac_decision2 == "[/]":
                    print("You can't sacrifice that card")
                    break
                elif sacrifice == "3" and sac_decision5 != "[/]":
                    damage2 = copy.copy(damage)
                    damage -= cardA3[2]
                    if damage < 0:
                        damage = 0
                    text = (f"Your {cardA3[0]} saved you from {damage2} damage, you only lose {damage} health")
                    print(text)
                    damageaverted = damage2 - damage
                    if damageaverted > damage2:
                        damageaverted = damage2
                    break
                elif sacrifice == "3" and sac_decision5 == "[/]":
                    print("You can't sacrifice that card")
                    break
                else:
                    print("Please select a creature to sacrifice")
    return damage, pHA, playerHealthA, handA, cardA1, cardA2, cardA3, damageaverted, text
def spell_execution():
    global creatureA
    global handA
    global handB
    global cardA1
    global cardA2
    global cardA3
    print(f"Your {creatureA[0]} was executed")
    creatureA = "default"
    if cardA1[0] == "Execution":
        cardA1 = "default"
    elif cardA2[0] == "Execution":
        cardA2 = "default"
    elif cardA3[0] == "Execution":
        cardA3 = "default"
    drawA()
    creatureSelection(handA, handB)
    strength_reduction()
    return creatureA, handA, creatureB
def spell_trap():
    global creatureB
    global trap
    global spellA
    global trapcounter

    if creatureB != "default":
        creatureB[1] -= 5
        creatureB[2] -= 5
        if creatureB[2] > 0:
            if creatureB[1] <= 0:
                creatureB[1] = 1
            print(f"Your enemys {creatureB[0]} has {creatureB[1]} strength and {creatureB[2]} health left")
        elif creatureB[2] <= 0:
            creatureB[2] = 0
            if creatureB[1] <= 0:
                creatureB[1] = 1
            print(f"Your enemys {creatureB[0]} is dead because of your Trap")
            trapcounter = 1
            creatureB = "default"
            creatureSelection(handA,handB)
            strength_reduction()
    elif creatureB == "default":
        print("You can't play a trap now")
    return creatureB, spellA, trapcounter

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
def creatureSelection(handA, handB):
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
    global spell_selection
    global counterdeploy
    global counterdeploy

    if creatureB == "default":
        cardB = copy.deepcopy(random.choice(handB))
        creatureB = cardB
        if firstround != 1:
            print(f"Your enemy delpoied a {creatureB[0]}")
        counterdeploy = 1
    if cardA1[3] == "creature" or cardA1 == "creatureE":
        creature_selection1 =("([1]")
        n1 =(cardA1[0])
        st1 = (cardA1[1])
        h1 = (cardA1[2])
        creature_selection3 =(")")
        choice1 = "1"
    elif cardA1[3] != "creature" or cardA1 != "creatureE":
        creature_selection1 =("([/]")
        n1 =(cardA1[0])
        st1 = ""
        h1 = ""
        creature_selection3 =(")")
        choice1 = "/"
    if cardA2[3] == "creature" or cardA2 == "creatureE":
        creature_selection4 =("([2]")
        n2 =(cardA2[0])
        st2 = (cardA2[1])
        h2 = (cardA2[2])
        creature_selection6 =(")")
        choice2 = "2"
    elif cardA2[3] != "creature" or cardA2 != "creatureE":
        creature_selection4 =("([/]")
        n2 =(cardA2[0])
        st2 = ""
        h2 = ""
        creature_selection6 =(")")
        choice2 = "/"
    if cardA3[3] == "creature" or cardA3 == "creatureE":
        creature_selection7 =("([3]")
        n3 =(cardA3[0])
        st3 = (cardA3[1])
        h3 = (cardA3[2])
        creature_selection9 =(")")
        choice3 = "3"
    elif cardA3[3] != "creature" or cardA3 != "creatureE":
        creature_selection7 =("([/]")
        n3 =(cardA3[0])
        st3 = ""
        h3 = ""
        creature_selection9 =(")")
        choice3 = "/"
    if creatureA == "default":
        # field_selection = ("[1]", cardA1[0], cardA1[1], cardA1[2], "[2]",cardA2[0], cardA2[1], cardA2[2], "[3]", cardA3[0], cardA3[1], cardA3[2])
        print(creature_selection1,n1,st1,h1,creature_selection3,creature_selection4,n2,st2,h2,creature_selection6,creature_selection7,n3,st3,h3,creature_selection9)
        while choice != "1" or "2" or "3":
            choice = input(f"Select a creature ({choice1}|{choice2}|{choice3}): ")
            if choice == "1" and cardA1[3] != "spell":
                cardA = copy.deepcopy(handA[0])
                creatureA = cardA
                choice = "0"
                counterdeploy = 1
                break
            elif choice == "2" and cardA2[3] != "spell":
                cardA = copy.deepcopy(handA[1])
                choice = "0"
                creatureA = cardA
                counterdeploy = 1
                break
            elif choice == "3" and cardA3[3] != "spell":
                cardA = copy.deepcopy(handA[2])
                creatureA = cardA
                choice = "0"
                counterdeploy = 1
                break
            else:
                print("please select a creature")
    return cardA, choice, cardB, creatureA, creatureB, spell_selection, spellA, spellB, counterdeploy, counterdeploy

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

# This function allows the player to choose spells
def spellSelection():
        global creatureA
        global creatureB
        global damage
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
        global startfightcounter
        if spellA == "default":
            while creatureB[3] != "default": 
                if cardA1[3] == "spell":
                    spell_selection1 = ("([1]")
                    spell_selection2 = (cardA1[0])
                    spell_selection3 = (")")
                    spell_choice1 = "1"
                elif cardA1[3] != "spell":
                    spell_selection1 = ("([/]")
                    spell_selection2 = (cardA1[0])
                    spell_selection3 = (")")
                    spell_choice1 = "/"
                if cardA2[3] == "spell":
                    spell_selection4 = ("([2]")
                    spell_selection5 = (cardA2[0])
                    spell_selection6 = (")")
                    spell_choice2 = "2"
                elif cardA2[3] != "spell":
                    spell_selection4 = ("([/]")
                    spell_selection5 = (cardA2[0])
                    spell_selection6 = (")")
                    spell_choice2 = "/"
                if cardA3[3] == "spell":
                   spell_selection7 = ("([3]")
                   spell_selection8 = (cardA3[0])
                   spell_selection9 = (")")
                   spell_choice3 = "3"
                elif cardA3[3] != "spell":
                    spell_selection7 = ("([/]")
                    spell_selection8 = (cardA3[0])
                    spell_selection9 = (")")
                    spell_choice3 = "/"
                if cardA1[3] == "spell" or cardA2[3] == "spell" or cardA3[3] == "spell":
                    print(spell_selection1,spell_selection2,spell_selection3,spell_selection4,spell_selection5,spell_selection6,spell_selection7,spell_selection8,spell_selection9)
                    spell_choice = input(f"Select a spell({spell_choice1}|{spell_choice2}|{spell_choice3})(Select nothing for no spell). enter to start fight ")
                    startfightcounter = 1
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
        return creatureA, creatureB, damage, playerHealthA, playerHealthB, damageaverted, spell_choice, spellA, spellB, cardA1, cardA2, cardA3 , spell_selection,

strengthA=0
strengthB=0
damage=0
playerHealthA = 20
playerHealthB = 20
pHA = 0
sA=0
sB=0
s3=0
s4=0
damageaverted = 0
startfightcounter = 0
trapcounter = 0

# this function does all the mathmatical stuff for the fights between the creatures ant it lowers the player health if it should get lower
def fight():
    global creatureA
    global creatureB
    global strengthA
    global strengthB
    global damage
    global playerHealthA
    global playerHealthB
    global sA
    global sB
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
    global startfightcounter
    drawA()
    drawB()
    roll()
    if startfightcounter == 0:
        print(input("enter to start fight "))
    startfightcounter = 0
    sA=copy.copy(creatureA[1])
    sB=copy.copy(creatureB[1])
    print("")
    print(f"Round {rounds}")
    print("Your Additional strength:",AdStrengthA)
    print("Your enemys Additional strength",AdStrengthB)
    strengthA = creatureA[1] + int(AdStrengthA)
    strengthB = creatureB[1] + int(AdStrengthB)
    if strengthA > strengthB:
        damage=strengthA - strengthB
        if damage > creatureB[2]:
            damage = damage - creatureB[2]
            creatureB[2]=0
            playerHealthB = playerHealthB - damage
            print(f"Your {creatureA[0]} wins with {strengthA} strenght against {strengthB} strength and inflicts {damage} damage to your enemy")
            if playerHealthB < 0:
                playerHealthB = 0
            print("Your enemy has",playerHealthB,"left")
        else:
            creatureB[2] = creatureB[2] - damage
            print(f"Your {creatureA[0]} wins with {strengthA} strenght against {strengthB} and inflicts {damage} damage to your enemys {creatureB[0]}")
    elif strengthA < strengthB:
        damage=strengthB - strengthA
        if damage > creatureA[2]:
            damage = damage - creatureA[2]
            creatureA[2]=0
            spell_sacrifice_shield1()
            playerHealthA = playerHealthA - damage
            spell_sacrifice_shield2()
            playerHealthA = playerHealthA + damageaverted
            damageaverted = 0
            text = "default"
            print(f"Your enemys {creatureB[0]} wins with {strengthB} strenght against {strengthA} strength and inflicts {damage} damage to you")
            if playerHealthA < 0:
                playerHealthA = 0
            print("You have",playerHealthA," health left")
        else:
            creatureA[2] = creatureA[2]- damage
            print(f"Your enemys {creatureB[0]} wins with {strengthB} strenght against {strengthA} strength and inflicts {damage} damage to your {creatureA[0]}")
    elif strengthA == strengthB:
        print("Draw")
    spell_selection = []
    return creatureA, creatureB, damage, playerHealthA, playerHealthB, damageaverted, spell_choice, spellA, spellB, cardA1, cardA2, cardA3 , spell_selection,

# These functions check if a creature or the player is dead, and it tracks the looses and the wins
def check1():
    global playerHealthA
    global playerHealthB
    if playerHealthA <= 0:
        print("You loose!")
        with open("stats.txt", "a") as s:
            s.write("loose\n")
    elif playerHealthB <= 0:
        with open("stats.txt", "a") as s:
            s.write("win\n")
        print("You win!")
    return playerHealthB, playerHealthA
    
def check2():
    global creatureA
    global creatureB
    global trapcounter
    global playerHealthA
    global playerHealthB
    if creatureA[2] <= 0:
        print("Your",creatureA[0] + "  is dead")
        strength_reduction()
        creatureA= "default"
        if len(deckA) == 0:
            playerHealthA = 0
            print("You have no cards left")
        if len(deckB) == 0:
            playerHealthB = 0
            print("Your enemy has no cards left")
    elif creatureB[2] <= 0 and trapcounter != 1:
        strength_reduction()
        print("Your enemys",creatureB[0] + " is dead")
        creatureB= "default"
        if len(deckA) == 0:
            playerHealthA = 0
            print("You have no cards left")
        if len(deckB) == 0:
            playerHealthB = 0
            print("Your enemy has no cards left")
    trapcounter = 0
    return creatureA,creatureB, rounds, trapcounter, playerHealthB, playerHealthA

rounds = 2
firstround = 1
counterdeploy = 0
counterdeploy = 1
# This countes the played rounds
def rounds_count():
    global rounds
    rounds += 1
    return rounds

# This lowers the strength of creatures
def strength_reduction():
    global creatureA
    global creatureB
    global counterdeploy
    global counterdeploy

    sA=copy.copy(creatureA[1])
    sB=copy.copy(creatureB[1])

    if counterdeploy != 1:
        creatureB[1] -= sA
        if creatureB[1] < 1:
            creatureB[1] = 1

    if counterdeploy != 1:
        creatureA[1] -= sB
        if creatureA[1] < 1:
            creatureA[1] = 1

    return creatureA, creatureB, counterdeploy, counterdeploy

def reset(playerHealthA,playerHealthB):
    playerHealthA = 20
    playerHealthB = 20
    return playerHealthA, playerHealthB
wins = 0
looses = 0
games = 0
def w_and_l(wins,looses,games):
    with open("stats.txt", "r") as s:
                for line in s:
                    if "win" in line:
                        wins += 1
                    if "loose" in line:
                        looses += 1
                    games += 1
    print(f"Games Played: {games}\nWins: {wins}\nLooses: {looses}")
    return wins, looses, games
# the menu
print("WELCOME TO JOLGERAT")
print(" ")
print("[1] Play")
print("[2] Tutorial")
print("[3] Stats")
print("[4] Credits")
print("[5] Exit")
firstChoice = input("1/2/3/4/5 ")
print("")
while firstChoice == "1"or"2"or"3"or"4"or"5":
    if firstChoice == "1": # playwin
        # The core
        while playerHealthA > 0 and playerHealthB > 0:
            drawA() 
            drawB()
            if firstround == 1:
                print(f"Round {firstround}")
            creatureSelection(handA,handB)
            removeFromHand()
            strength_reduction()
            print("You:",creatureA[0],"S:",creatureA[1],"H:",creatureA[2])
            print("Enemy:",creatureB[0],"S:",creatureB[1],"H:",creatureB[2])
            spellSelection()
            counterdeploy = 0
            fight()
            check2()
            check1()
            rounds_count()
            firstround = 2
        reset(playerHealthA,playerHealthB)
        print(" ")
        input("enter to go back to main menu ")
        print(" ")
        print("[1] Play")
        print("[2] Tutorial")
        print("[3] Stats")
        print("[4] Credits")
        print("[5] Exit")
        firstChoice = input("1/2/3/4/5 ")
        print("")
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
        print("")
    elif firstChoice == "3": # Stats 
        w_and_l(wins,looses,games)
        input("enter to go back to main menu ")
        print(" ")
        print("[1] Play")
        print("[2] Tutorial")
        print("[3] Stats")
        print("[4] Credits")
        print("[5] Exit")
        firstChoice = input("1/2/3/4/5 ")
        print("")
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
        print("")
    elif firstChoice == "5": # Exit 
        exitchoice = input("Do you want to exit the game?[y/n] ")
        if exitchoice == "y":
            sys.exit()
        else:
            print("[1] Play")
            print("[2] Tutorial")
            print("[3] Stats")
            print("[4] Credits")
            print("[5] Exit")
            firstChoice = input("1/2/3/4/5 ")
            print("")

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