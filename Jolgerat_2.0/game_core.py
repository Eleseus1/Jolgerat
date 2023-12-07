# Imports
import random as r
import copy as c
import variables as v

def creature_choice():
    choices = []
    c_list = []
    c1 = "default"
    c2 = "default"
    c3 = "default"
    for card in v.handA:
        counter = 1

        if card[3] == 0 or 1:
            choices.append(f"[/] {card[0]} {card[1]} {card[2]}")
            c_list.append["[/]"]
        else:
            choices.append(f"[{counter}] {card[0]} {card[1]} {card[2]}")
            c_list.append[f"[{counter}]"]

        " / ".join(choices)
        counter += 1

    choice = input("()")

#  check_card for health and when health under 1 remove the card
def check_card(field):
    if field[2] < 1:
        field = 'default'

def dice():
    aditional_strenght_a = r.randint(1, 6)
    aditional_strenght_b = r.randint(1, 6)

    return aditional_strenght_a, aditional_strenght_b