import random
import copy  
import sys
import Jolgerat_draw as d
import Jolgerat_Effect_Creatures as e

# To do:
# Fix damage calculation and fix e creatures
# Deck editor
# info function
# Update turtorial

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
    d.draw()
    creatureSelection(d.handA,d.handB)
    removeFromHand()
    e.eactivation(creatureA,creatureB,deploycounterA,deploycounterB)
    creatureSelection(d.handA,d.handB)
    removeFromHand()
    strength_reduction()
    return creatureA,creatureB
def spell_sacrifice_shield1(): 
    global playerHealthA
    global pHA
    global sac_decision
    global damage
    if playerHealthA != pHA:
        pHA = copy.copy(playerHealthA)
    return playerHealthA,pHA
def spell_sacrifice_shield2():
    global playerHealthA
    global pHA
    global damage
    global damageaverted
    global text
    global cardA
    global cardB
    if playerHealthA < pHA and d.sacrifice_shield in d.handA:
        choice = input("You are about to take " + str(damage) + " damage! Do you want to use a Sacrifice Shield?[y/n] ")
        if choice == "y":
            if d.cardA1 == d.sacrifice_shield:
                d.cardA1 = "default"
                d.draw()
            elif d.cardA2 == d.sacrifice_shield:
                d.cardA2 = "default"
                d.draw()
            elif d.cardA3 == d.sacrifice_shield:
                d.cardA3 = "default"
                d.draw()

            if d.cardA1[3] == "creature" or d.cardA1[3] == "creatureE" and d.cardA1[0] != "Jester":
                sac_decision1 =("[1]")
                sac_decision2 =(d.cardA1[0],d.cardA1[1],d.cardA1[2])
            elif d.cardA1[3] != "creature" or d.cardA1[3] != "creatureE" or d.cardA1[0] == "Jester":
                sac_decision1 =("[/]")
                sac_decision2 =("")
            if d.cardA2[3] == "creature" or d.cardA2[3] == "creatureE" and d.cardA2[0] != "Jester":
                sac_decision3 =("[2]")
                sac_decision4 =(d.cardA2[0],d.cardA2[1],d.cardA2[2])
            elif d.cardA2[3] != "creature" or d.cardA2[3] != "creatureE" or d.cardA2[0] == "Jester":
                sac_decision3 =("[/]")
                sac_decision4 =("")
            if d.cardA3[3] == "creature" or d.cardA3[3] == "creatureE" and d.cardA3[0] != "Jester":
                sac_decision5 =("[3]")
                sac_decision6 =(d.cardA3[0],d.cardA3[1],d.cardA3[2])
            elif d.cardA3[3] != "creature" or d.cardA3[3] != "creatureE" or d.cardA3[0] == "Jester":
                sac_decision5 =("[/]")
                sac_decision6 =("")
            print(sac_decision1, sac_decision2, sac_decision3, sac_decision4, sac_decision5, sac_decision6)
            sacrifice = input("(" + sac_decision1 + sac_decision3 + sac_decision5 + ") ")
            while sacrifice != "1" or "2" or "3":
                if sacrifice == "1" and sac_decision1 != "[/]":
                    damage2 = copy.copy(damage)
                    damage -= d.cardA1[2]
                    if damage < 0:
                        damage = 0
                    text = (f"Your {d.cardA1[0]} saved you from {damage2} damage, you only lose {damage} health")
                    if damage == 0:
                        text = (f"Your {d.cardA1[0]} saved you from {damage2} damage, you lose no health")
                    print(text)
                    damageaverted = damage2 - damage
                    if damageaverted > damage2:
                        damageaverted = damage2
                    cardA = d.cardA1
                    removeFromHand()
                    break
                elif sacrifice == "1" and sac_decision1 == "[/]":
                    print("You can't sacrifice that card")
                    break
                elif sacrifice == "2" and sac_decision3 != "[/]":
                    damage2 = copy.copy(damage)
                    damage = damage - d.cardA2[2]
                    if damage < 0:
                        damage = 0
                    text = (f"Your {d.cardA2[0]} saved you from {damage2} damage, you only lose {damage} health")
                    if damage == 0:
                        text = (f"Your {d.cardA2[0]} saved you from {damage2} damage, you lose no health")
                    print(text)
                    damageaverted = damage2 - damage
                    if damageaverted > damage2:
                        damageaverted = damage2
                    cardA = d.cardA2
                    removeFromHand()
                    break
                elif sacrifice == "2" and sac_decision2 == "[/]":
                    print("You can't sacrifice that card")
                    break
                elif sacrifice == "3" and sac_decision5 != "[/]":
                    damage2 = copy.copy(damage)
                    damage -= d.cardA3[2]
                    if damage < 0:
                        damage = 0
                    text = (f"Your {d.cardA3[0]} saved you from {damage2} damage, you only lose {damage} health")
                    if damage == 0:
                        text = (f"Your {d.cardA3[0]} saved you from {damage2} damage, you lose no health")
                    print(text)
                    damageaverted = damage2 - damage
                    if damageaverted > damage2:
                        damageaverted = damage2
                    cardA = d.cardA3
                    removeFromHand()
                    break
                elif sacrifice == "3" and sac_decision5 == "[/]":
                    print("You can't sacrifice that card")
                    break
                else:
                    print("Please select a creature to sacrifice")
    return damage, pHA, playerHealthA, d.handA, d.cardA1, d.cardA2, d.cardA3, damageaverted, text
def spell_execution():
    global creatureA
    print(f"Your {creatureA[0]} was executed")
    creatureA = "default"
    if d.cardA1[0] == "Execution":
        d.cardA1 = "default"
    elif d.cardA2[0] == "Execution":
        d.cardA2 = "default"
    elif d.cardA3[0] == "Execution":
        d.cardA3 = "default"
    d.draw()
    creatureSelection(d.handA, d.handB)
    removeFromHand()
    e.eactivation(creatureA,creatureB,deploycounterA,deploycounterB)
    creatureSelection(d.handA,d.handB)
    removeFromHand()
    strength_reduction()
    return creatureA, d.handA, d.handB, creatureB
def spell_trap():
    global creatureB
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
            creatureSelection(d.handA,d.handB)
            removeFromHand()
            e.eactivation(creatureA,creatureB,deploycounterA,deploycounterB)
            creatureSelection(d.handA,d.handB)
            removeFromHand()
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
    global choice
    global spell_choice
    global creatureA
    global creatureB
    global spellA
    global spellB
    global deploycounter
    global deploycounterA
    global deploycounterB
    global cardA
    global cardB

    if creatureB == "default":
        cardB = copy.deepcopy(random.choice(d.handB))
        creatureB = cardB
        if firstround != 1:
            print(f"Your enemy delpoied a {creatureB[0]}")
        deploycounter = True
        deploycounterB = True
    if d.cardA1[3] == "creature" or d.cardA1[3] == "creatureE":
        creature_selection1 =("([1]")
        n1 =(d.cardA1[0])
        st1 = (d.cardA1[1])
        h1 = (d.cardA1[2])
        creature_selection3 =(")")
        choice1 = "1"
    elif d.cardA1[3] != "creature" or d.cardA1[3] != "creatureE":
        creature_selection1 =("([/]")
        n1 =(d.cardA1[0])
        st1 = ""
        h1 = ""
        creature_selection3 =(")")
        choice1 = "/"
    if d.cardA2[3] == "creature" or d.cardA2[3] == "creatureE":
        creature_selection4 =("([2]")
        n2 =(d.cardA2[0])
        st2 = (d.cardA2[1])
        h2 = (d.cardA2[2])
        creature_selection6 =(")")
        choice2 = "2"
    elif d.cardA2[3] != "creature" or d.cardA2[3] != "creatureE":
        creature_selection4 =("([/]")
        n2 =(d.cardA2[0])
        st2 = ""
        h2 = ""
        creature_selection6 =(")")
        choice2 = "/"
    if d.cardA3[3] == "creature" or d.cardA3[3] == "creatureE":
        creature_selection7 =("([3]")
        n3 =(d.cardA3[0])
        st3 = (d.cardA3[1])
        h3 = (d.cardA3[2])
        creature_selection9 =(")")
        choice3 = "3"
    elif d.cardA3[3] != "creature" or d.cardA3[3] != "creatureE":
        creature_selection7 =("([/]")
        n3 =(d.cardA3[0])
        st3 = ""
        h3 = ""
        creature_selection9 =(")")
        choice3 = "/"
    if creatureA == "default":
        # field_selection = ("[1]", d.cardA1[0], d.cardA1[1], d.cardA1[2], "[2]",d.cardA2[0], d.cardA2[1], d.cardA2[2], "[3]", d.cardA3[0], d.cardA3[1], d.cardA3[2])
        print(creature_selection1,n1,st1,h1,creature_selection3,creature_selection4,n2,st2,h2,creature_selection6,creature_selection7,n3,st3,h3,creature_selection9)
        while choice != "1" or "2" or "3":
            choice = input(f"Select a creature ({choice1}|{choice2}|{choice3}): ")
            if choice == "1" and d.cardA1[3] != "spell" and d.cardA1[3] != "spellspecial":
                cardA = copy.deepcopy(d.cardA1)
                creatureA = cardA
                choice = "0"
                deploycounter = True
                deploycounterA = True
                break
            elif choice == "2" and d.cardA2[3] != "spell" and d.cardA2[3] != "spellspecial":
                cardA = copy.deepcopy(d.cardA2)
                choice = "0"
                creatureA = cardA
                deploycounter = True
                deploycounterA = True
                break
            elif choice == "3" and d.cardA3[3] != "spell" and d.cardA3[3] != "spellspecial":
                cardA = copy.deepcopy(d.cardA3)
                creatureA = cardA
                choice = "0"
                deploycounter = True
                deploycounterA = True
                break
            else:
                print("please select a creature")
    return cardA, choice, cardB, creatureA, creatureB, spellA, spellB, deploycounter, deploycounter, d.handA, d.handB, d.cardA1, d.cardA2, d.cardA3, d.cardB1, d.cardB2, d.cardB3

# This function removes cards from the hands # to do
def removeFromHand():
    global cardA
    global cardB
    if cardA == d.cardA1:
        d.cardA1 = "default"
        d.draw()
    elif cardA == d.cardA2:
        d.cardA2 = "default"
        d.draw()
    elif cardA == d.cardA3:
        d.cardA3 = "default"
        d.draw()
    elif cardB == d.cardB1:
        d.cardB1 = "default"
        d.draw()
    elif cardB == d.cardB2:
        d.cardB2 = "default"
        d.draw()
    elif cardB == d.cardB3:
        d.cardB3 = "default"
        d.draw()
    
    return d.cardA1,d.cardA2,d.cardA3,d.cardB1,d.cardB2,d.cardB3,cardA,cardB,d.handB,d.handA,d.deckA,d.deckB

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
        global cardA
        global startfightcounter
        if spellA == "default":
            while creatureB[3] != "default": 
                if d.cardA1[3] == "spell":
                    spell_selection1 = ("([1]")
                    spell_selection2 = (d.cardA1[0])
                    spell_selection3 = (")")
                    spell_choice1 = "1"
                elif d.cardA1[3] != "spell":
                    spell_selection1 = ("([/]")
                    spell_selection2 = (d.cardA1[0])
                    spell_selection3 = (")")
                    spell_choice1 = "/"
                if d.cardA2[3] == "spell":
                    spell_selection4 = ("([2]")
                    spell_selection5 = (d.cardA2[0])
                    spell_selection6 = (")")
                    spell_choice2 = "2"
                elif d.cardA2[3] != "spell":
                    spell_selection4 = ("([/]")
                    spell_selection5 = (d.cardA2[0])
                    spell_selection6 = (")")
                    spell_choice2 = "/"
                if d.cardA3[3] == "spell":
                   spell_selection7 = ("([3]")
                   spell_selection8 = (d.cardA3[0])
                   spell_selection9 = (")")
                   spell_choice3 = "3"
                elif d.cardA3[3] != "spell":
                    spell_selection7 = ("([/]")
                    spell_selection8 = (d.cardA3[0])
                    spell_selection9 = (")")
                    spell_choice3 = "/"
                if d.cardA1[3] == "spell" or d.cardA2[3] == "spell" or d.cardA3[3] == "spell":
                    print(spell_selection1,spell_selection2,spell_selection3,spell_selection4,spell_selection5,spell_selection6,spell_selection7,spell_selection8,spell_selection9)
                    spell_choice = input(f"Select a spell({spell_choice1}|{spell_choice2}|{spell_choice3})(Select nothing for no spell). enter to start fight ")
                    startfightcounter = 1
                    if spell_choice == "1" and d.cardA1[3] == "spell":
                        spellA = d.cardA1
                        spellcasting(d.cardA1)
                        cardA = spellA
                        removeFromHand()
                        spellA = "default"
                        break
                    elif spell_choice == "2" and d.cardA2[3] == "spell":
                        spellA = d.cardA2
                        spellcasting(d.cardA2)
                        cardA = spellA
                        removeFromHand()
                        spellA = "default"
                        break
                    elif spell_choice == "3" and d.cardA3[3] == "spell":
                        spellA = d.cardA3
                        spellcasting(d.cardA3)
                        cardA = spellA
                        removeFromHand()
                        spellA = "default"
                        break
                    else:
                       break
                else:
                    break
        return creatureA, creatureB, damage, playerHealthA, playerHealthB, damageaverted, spell_choice, spellA, spellB, d.cardA1, d.cardA2, d.cardA3

strengthA=0
strengthB=0
damage=0
playerHealthA = 20
playerHealthB = 20
pHA = 0
sA=0
sB=0
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
    global cardA
    global startfightcounter
    d.draw()
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
    return creatureA, creatureB, damage, playerHealthA, playerHealthB, damageaverted, spell_choice, spellA, spellB, d.cardA1, d.cardA2, d.cardA3

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
    if creatureA[2] <= 0 and creatureA[0] != "Ghost":
        print("Your",creatureA[0] + "  is dead")
        strength_reduction()
        e.eactivation(creatureA,creatureB,deploycounterA,deploycounterB)
        creatureA= "default"
        if len(d.deckA) == 0:
            playerHealthA = 0
            print("You have no cards left")
        if len(d.deckB) == 0:
            playerHealthB = 0
            print("Your enemy has no cards left")
    elif creatureB[2] <= 0 and trapcounter != 1 and creatureB[0] != "Ghost":
        strength_reduction()
        print("Your enemys",creatureB[0] + " is dead")
        e.eactivation(creatureA,creatureB,deploycounterA,deploycounterB)
        creatureB= "default"
        if len(d.deckA) == 0:
            playerHealthA = 0
            print("You have no cards left")
        if len(d.deckB) == 0:
            playerHealthB = 0
            print("Your enemy has no cards left")
    trapcounter = 0
    return creatureA,creatureB, rounds, trapcounter, playerHealthB, playerHealthA

rounds = 2
firstround = 1
deploycounter = False
deploycounterA = False
deploycounterB = False
# This countes the played rounds
def rounds_count():
    global rounds
    rounds += 1
    return rounds

# This lowers the strength of creatures
def strength_reduction():
    global creatureA
    global creatureB
    global deploycounter

    sA=copy.copy(creatureA[1])
    sB=copy.copy(creatureB[1])

    if deploycounter == False and creatureB[0] != "Ghost":
        creatureB[1] -= sA
        if creatureB[1] < 1:
            creatureB[1] = 1
    if deploycounter == False and creatureA[0] != "Ghost":
        creatureA[1] -= sB
        if creatureA[1] < 1:
            creatureA[1] = 1

    if deploycounter == False and creatureA[0] == "Ghost":
        creatureA[1] -= sB
        if creatureA[1] <= 0:
            creatureA[1] = 0
            print("Your",creatureA[0] + "  is dead")
            creatureA= "default"
            creatureSelection(d.handA,d.handB)
            removeFromHand()
            e.eactivation(creatureA,creatureB,deploycounterA,deploycounterB)
    if deploycounter == False and creatureB[0] == "Ghost":
        creatureB[1] -= sA
        if creatureB[1] <= 0:
            creatureB[1] = 0
            print("Your enemys",creatureB[0] + " is dead")
            creatureB = "default"
            creatureSelection(d.handA,d.handB)
            removeFromHand()
            e.eactivation(creatureA,creatureB,deploycounterA,deploycounterB)
            
    return creatureA, creatureB, deploycounter

def reset(playerHealthA,playerHealthB): # Tis resets the game so you can play two times without restarting
    playerHealthA = 20
    playerHealthB = 20
    d.deckA = copy.deepcopy(d.standardDeckA)
    d.deckB = copy.deepcopy(d.standardDeckB)
    return playerHealthA, playerHealthB, d.deckA, d.deckB
wins = 0
looses = 0
games = 0
def w_and_l(wins,looses,games): # If you want to test this function without playing games just write "win" and "loose" as often as you want in stats.txt(everything needs an own line)
    with open("stats.txt", "r") as s:
                for line in s:
                    if "win" in line:
                        wins += 1
                    if "loose" in line:
                        looses += 1
                    games += 1
    print(f"Games Played: {games}\nWins: {wins}\nLooses: {looses}")
    return wins, looses, games

one = 0
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
    playcounter = 1
    turtorialcounter = 1
    statscounter = 1
    creditscounter = 1
    exitcounter = 1
    deckeditorcounter = 1
    mistakecounter = 1
    if one == 1:
        print(" ")
        print("[1] Play")
        print("[2] Tutorial")
        print("[3] Stats")
        print("[4] Credits")
        print("[5] Exit")
        firstChoice = input("1/2/3/4/5 ")
        print("")
    one = 1
    if firstChoice == "1": # play
        # The core
        while playcounter == 1:
           while playerHealthA > 0 and playerHealthB > 0:
            d.draw()
            if firstround == 1:
                print(f"Round {firstround}")
            creatureSelection(d.handA,d.handB)
            removeFromHand()
            e.eactivation(creatureA,creatureB,deploycounterA,deploycounterB)
            creatureSelection(d.handA,d.handB)
            removeFromHand()
            strength_reduction()
            print("You:",creatureA[0],"S:",creatureA[1],"H:",creatureA[2])
            print("Enemy:",creatureB[0],"S:",creatureB[1],"H:",creatureB[2])
            spellSelection()
            deploycounter = False
            deploycounterA = False
            deploycounterB = False
            fight()
            check2()
            check1()
            rounds_count()
            firstround = 2
        reset(playerHealthA,playerHealthB)
        input("enter to go back to main menu ")
        print("")
        playcounter = 2 
    elif firstChoice == "2": # Turtorial
        while turtorialcounter == 1:
            print("The turtorial is not done yet")
            turtorialcounter = input("enter to go back to main menu ")
            print("")
    elif firstChoice == "3": # Stats
        while statscounter == 1: 
            w_and_l(wins,looses,games)
            statscounter = input("enter to go back to main menu ")
            print("")
    elif firstChoice == "4": # Credits
        while creditscounter == 1:
            print("Eleseus")
            print("DVillablanca")
            print("Chat GPT")
            creditscounter = input("enter to go back to main menu ")
            print("")
    elif firstChoice == "5": # Exit 
        while exitcounter == 1:
            exitchoice = input("Do you want to exit the game?[y/n] ")
            if exitchoice == "y":
               sys.exit()
            else:
                exitcounter = input("enter to go back to main menu ")
                print("")
    else:
        while mistakecounter == 1:
           print(f"{firstChoice} is not an option")
           mistakecounter = 2

# I used this codeblock to test everything
"""
drawA()
drawB()
cardSelection(handA,handB)
print("Your card: ",fieldA[0],"S:",fieldA[1],"H:" fieldA[3])
print("Opponents card",fieldB[0],"S:",fieldB[2],"H:",fieldB[3])
removeFromHand()
fight(fieldA,fieldB)
drawA()
drawB()
cardSelection(handA,handB)
print("Your card: ",fieldA[0],"S:",fieldA[1],"H:",fieldA[3])
print("Opponents card",fieldB[0],"S:",fieldB[2],"H:",fieldB[3])
"""