# Imports
import random as r
import copy as c
import variables as v
import draw as d

def creature_choice():
    choices = []
    c_list = []
    c1 = "default"
    c2 = "default"
    c3 = "default"
    counter = 1
    for card in v.handA:
        if card[3] == 0:
            choices.append(f"[/] {card[0]}")
            c_list.append("[/]")
        else:
            choices.append(f"[{str(counter)}] {card[0]} {card[1]} {card[2]}")
            c_list.append(f"[{str(counter)}]")

        counter += 1
    
    print(f"{choices[0]} / {choices[1]} / {choices[2]}")
    choice = input(f"({c_list[0]}/{c_list[1]}/{c_list[2]}) ")

#  check_card for health and when health under 1 remove the card
def check_card(field):
    if field[2] < 1:
        field = 'default'

def dice():
    aditional_strenght_a = r.randint(1, 6)
    aditional_strenght_b = r.randint(1, 6)

    return aditional_strenght_a, aditional_strenght_b

d.draw()
creature_choice()