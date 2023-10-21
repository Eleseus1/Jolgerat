import Jolgerat_draw as d
import random as r
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
                e_cursedmagician(creatureA)
        elif creatureA[0] == "Jester" and deploycounterA == True:
                e_jester(creatureA,creatureB)
        elif creatureA[0] == "Mask Master" and creatureA[2] == 0:
                e_maskmaster(d.deckA,creatureA)
    if creatureB[3] == "creatureE":
        if creatureB[0] == "Starcatcher" and creatureB[2] == 0:
                e_starcatcher(creatureB,creatureA)
        elif creatureB[0] == "Cursed Magician" and deploycounterB == True:
                e_cursedmagician(creatureB)
        elif creatureB[0] == "Jester" and deploycounterB == True:
                e_jester(creatureB,creatureA)
        elif creatureB[0] == "Mask Master" and creatureB[2] == 0:
                e_maskmaster(d.deckB,creatureB)

# The effects of the creatures
def e_starcatcher(creatureA,creatureB):
    creatureA = "default"
    creatureB = "default"
    d.handA[0] =  "default"
    d.handA[1] =  "default"
    d.handA[2] =  "default"
    d.handB[0] =  "default"
    d.handB[1] =  "default"
    d.handB[2] =  "default"
    print("The Starcatcher died, the field and all hands are empty now")
    return creatureA, creatureB, d.handA[0], d.handA[1], d.handA[2], d.handB[0], d.handB[1], d.handB[2]
def e_cursedmagician(creature):
    creature[1] += r.randint(2,12)
    creature[2] += r.randint(1,6)
    print(f"Your {creature[0]} spawns with {creature[1]} strength and {creature[2]} health")
    return creature
def e_jester(creatureA,creatureB):
    creatureA[1] = creatureB[1]
    creatureA[2] = creatureB[2]
    print(f"Your Jester is now equal to your enemys {creatureB[0]}")
    return creatureA, creatureB
def e_maskmaster(deck,creature):
        creatures = [card for card in deck if card[3] != "spell" and card[3] != "spellspecial"]
        creature == r.choice(creatures)
        print(f"Your Mask Master turned into a {creature[0]}")
        creature[1] -= 2
        creature[2] -= 2
        return deck, creature