import Jolgerat_draw as d
import random as r
import copy as c
# The effect "launcher"
def eactivation(creatureA,creatureB,deploycounterA,deploycounterB):
    if creatureA[2] < 0:
        creatureA[2] = 0
    if creatureB[2] < 0:
        creatureB[2] = 0
    if creatureA[3] == "creatureE":
        if creatureA[0] == "Starcatcher" and creatureA[2] == 0:
                e_starcatcher(creatureA,creatureB)
        elif creatureA[0] == "Cursed Magician" and deploycounterA == True:
                counter_ = "A"
                e_cursedmagician(creatureA,counter_)
        elif creatureA[0] == "Jester" and deploycounterA == True:
                counter = "A"
                e_jester(creatureA,creatureB,counter)
        elif creatureA[0] == "Mask Master" and creatureA[2] == 0:
                e_maskmaster(d.deckA,creatureA)
    if creatureB[3] == "creatureE":
        if creatureB[0] == "Starcatcher" and creatureB[2] == 0:
                e_starcatcher(creatureB,creatureA)
        elif creatureB[0] == "Cursed Magician" and deploycounterB == True:
                counter_ = "B"
                e_cursedmagician(creatureB,counter_)
        elif creatureB[0] == "Jester" and deploycounterB == True:
                counter = "B"
                e_jester(creatureB,creatureA,counter)
        elif creatureB[0] == "Mask Master" and creatureB[2] == 0:
                e_maskmaster(d.deckB,creatureB)
        return creatureA, creatureB

# The effects of the creatures
def e_starcatcher(creatureA,creatureB):
    creatureA = "default"
    creatureB = "default"
    d.cardA1 =  "default"
    d.cardA2 =  "default"
    d.cardA3 =  "default"
    d.cardB1 =  "default"
    d.cardB2 =  "default"
    d.cardB3 =  "default"
    print("The Starcatcher died, the field and all hands are empty now")
    d.draw()
    return creatureA, creatureB, d.cardA1, d.cardA2, d.cardA3, d.cardB1, d.cardB2, d.cardB3
def e_cursedmagician(creature,counter):
    creature[1] += r.randint(2,12)
    creature[2] += r.randint(1,6)
    if counter == "A":
        print(f"Your {creature[0]} spawns with {creature[1]} strength and {creature[2]} health")
    if counter == "B":
        print(f"Your enemys {creature[0]} spawns with {creature[1]} strength and {creature[2]} health")
    return creature
def e_jester(creatureA,creatureB,counter):
    creatureA[1] = creatureB[1]
    creatureA[2] = creatureB[2]
    if creatureA[0] == "Jester" and creatureB[0] == "Jester":
          creatureA[1] = 5
          creatureA[2] = 5
          creatureB[1] = 5
          creatureB[2] = 5
    if creatureA[0] == "Jester" and creatureB[0] == "Ghost":
          creatureA[1] = creatureB[1]
          creatureA[2] = 1
    if creatureA[0] == "Jester" and creatureB[0] == "Cursed Magician":
          counterC = "/"
          e_cursedmagician(creatureA,counterC)
    if counter == "A":
        print(f"Your Jester copied your enemys {creatureB[0]}")
    if counter == "B":
        print(f"Your enemys Jester copied your {creatureB[0]}")
    return creatureA, creatureB
def e_maskmaster(deck,creature):
        creatures = c.deepcopy(deck)
        creatures = [card for card in deck if card[3] != "spell" and card[3] != "spellspecial"]
        creature == r.choice(creatures)
        if deck == d.deckA:
            print(f"Your Mask Master turned into a {creature[0]}")
        if deck == d.deckB:
            print(f"Your enemys Mask Master turned into a {creature[0]}")
        creature[1] += 2
        creature[2] += 2
        return creature