import random as r
import copy as c
import variables as v

# This changes the cards from player A
def drawA():

    if v.cardA1 == "default":
        v.cardA1 = c.deepcopy(r.choice(v.deckA))
        v.deckA.remove(v.cardA1)

    if v.cardA2 == "default":
        v.cardA2 = c.deepcopy(r.choice(v.deckA))
        v.deckA.remove(v.cardA2)

    if v.cardA3 == "default":
        v.cardA3 = c.deepcopy(r.choice(v.deckA))
        v.deckA.remove(v.cardA3)

    v.handA = [v.cardA1,v.cardA2, v.cardA3]
    if v.cardA1[3] != 0 and v.cardA1[3] != "1" and v.cardA2[3] != 0 and v.cardA2[3] != "1" and v.cardA3[3] != 0 and v.cardA3[3] != "1":
        print("You have no creature, select a card to discard")
        print("[1]",v.cardA1[0],"[2]",v.cardA2[0],"[3]",v.cardA3[0])
        discard_choice = input("(1|2|3) ")
        if discard_choice == "1":
            v.cardA1 = "default"
            drawA()
        elif discard_choice == "2":
            v.cardA2 = "default"
            drawA()
        elif discard_choice == "3":
            v.cardA3 = "default"
            drawA()

# This changes the cards from player B
def drawB():

    if v.cardB1 == "default":
        v.cardB1 = c.deepcopy(r.choice(v.deckB))
        v.deckB.remove(v.cardB1)

    if v.cardB2 == "default":
        v.cardB2 = c.deepcopy(r.choice(v.deckB))
        v.deckB.remove(v.cardB2)

    if v.cardB3 == "default":
        v.cardB3 = c.deepcopy(r.choice(v.deckB))
        v.deckB.remove(v.cardB3)

    v.handB = [v.cardB1, v.cardB2, v.cardB3]

def draw():
    drawA()
    drawB()

draw()
print(v.handA)
print(v.handB)