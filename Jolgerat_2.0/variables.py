import copy as c

# Deck variables

# The creatures (0:names,1:strength,2:health,3:class,4:effect index(0 = no effect))
knight = ["Knight",6, 12, 2, 0]
demon = ["Demon",15,10,2, 0]
prince = ["Prince",7,7,2, 0]
crow = ["Crow",5,3,2, 0]
skeleton = ["Skeleton",10,5,2, 0]

# Effect creatures ( card[3] == 0:names,1:strength,2:health,3:class,4:effect index)
jester = ["Jester",0,0,1,1]
maskmaster = ["Mask Master",10,8,1,2]
starcatcher = ["Starcatcher",12,15,1,3]
ghost = ["Ghost",18,0,1,4]
cursedmagician = ["Cursed Magician",1,1,1,5]

# The Spells (0:names,1:placeholder,2:placeholder,3:class,4:effect index)
joker = ["Joker","","", 0, 1]
sacrifice_shield = ["Sacrifice Shield","","", 0, 2] # This is special because you can't play the spell whenever you want, you have to wait untill you get damage and then you get asked if you want to play it
execution = ["Execution","","",0, 3]
smith = ["Smith","","",0, 4]
trap = ["Trap","","",0, 5]

# The decks
deckA = [
    knight, knight, knight, knight, demon, demon, crow, crow, crow, crow, crow, prince, prince, prince, prince, skeleton, skeleton, skeleton, skeleton, # Creatures
    #jester, jester, maskmaster, starcatcher, ghost, cursedmagician, cursedmagician, # Effect creatures
    #joker, sacrifice_shield, sacrifice_shield, execution, execution, execution, smith, smith, smith, trap, trap # Spells
    ]

# Deck B is an exact copy of deck A
deckB = []
for card in deckA:
    if card[3] == 1 or card[3] == 2:
        deckB.append(card)

# These are backups for the decks it´s needed if you want to play more then one game in a row
standardDeckA = c.deepcopy(deckA)
standardDeckB = c.deepcopy(standardDeckA)
# This removes all spells from deck B because I don´t know how to let the bot use them correctly 
standardDeckB = [card for card in standardDeckB if card[3] != 0]

# Hand A
cardA1 = "default"
cardA2 = "default"
cardA3 = "default"
handA = "default"

# Hand B
cardB1 = "default"
cardB2 = "default"
cardB3 = "default"
handB = "default"

# Game core variables 

fieldA = "default"
fieldB = "default"

spallA = "default"
spellB = "default"