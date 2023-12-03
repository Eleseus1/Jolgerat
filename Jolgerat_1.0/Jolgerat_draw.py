import random
import copy

# The creatures (0:names,1:strength,2:health,3:class)
knight = ["Knight",6,12,"creature"]
demon = ["Demon",15,10,"creature"]
prince = ["Prince",7,7,"creature"]
crow = ["Crow",5,3,"creature"]
skeleton = ["Skeleton",10,5,"creature"]
# Effect creatures
jester = ["Jester",0,0,"creatureE"]
maskmaster = ["Mask Master",10,8,"creatureE"]
starcatcher = ["Starcatcher",12,15,"creatureE"]
ghost = ["Ghost",18,0,"creatureE"]
cursedmagician = ["Cursed Magician",1,1,"creatureE"]
# The spells (0:names,1:placeholder,2:placeholder,3:class)
joker = ["Joker","","","spell"]
sacrifice_shield = ["Sacrifice Shield","","","spellspecial"] # This is "spellspecial" because you can't play the spell whenever you want, you have to wait untill you get damage and then you get asked if you want to play it
execution = ["Execution","","","spell"]
smith = ["Smith","","","spell"]
trap = ["Trap","","","spell"]

# The decks
deckA = [
    knight, knight, knight, knight, demon, demon, crow, crow, crow, crow, crow, prince, prince, prince, prince, skeleton, skeleton, skeleton, skeleton, # Creatures
    jester, jester, maskmaster, starcatcher, ghost, cursedmagician, cursedmagician, # Effect creatures
    joker, sacrifice_shield, sacrifice_shield, execution, execution, execution, smith, smith, smith, trap, trap # Spells
    ]
deckB = copy.deepcopy(deckA)
deckB = [card for card in deckB if card[3] != "spell" and card[3] != "spellspecial"]

standardDeckA = copy.deepcopy(deckA)
standardDeckB = copy.deepcopy(standardDeckA)
standardDeckB = [card for card in standardDeckB if card[3] != "spell" and card[3] != "spellspecial"]

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

def draw():
    drawA()
    drawB()
    return cardB1, cardB2, cardB3, deckB, handB, cardA1, cardA2, cardA3, deckA, handA
