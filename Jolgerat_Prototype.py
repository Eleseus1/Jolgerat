import random

#The cards(2= lives, 3= Atack points)
knight = ["Knight" , 6 , 12]
demon = ["Demon" , 10 , 15]
skeleton = ["Skeleton" , 5 , 10]
crow = ["Crow" , 3 , 5]
prince = ["Prince" , 7 , 7]

#The decks
deckR = [knight , knight , knight , knight , demon , demon , skeleton , skeleton , skeleton , skeleton , crow , crow , crow , crow , crow , crow , prince, prince, prince, prince]
deckB = [knight , knight , knight , knight , demon , demon , skeleton , skeleton , skeleton , skeleton , crow , crow , crow , crow , crow , crow , prince, prince, prince, prince]

#The cards that the players draw
handR = random.choice(deckR)
