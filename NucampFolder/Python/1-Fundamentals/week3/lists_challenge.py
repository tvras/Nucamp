'''
Code Challenge: Lists
Tierry
03/14/23
'''


import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_choice = input("Press enter to pick a card, or Q to exit:\t").lower()
    if user_choice == "q":
        break
    else: 
       card = random.choice(diamonds)
       hand.append(card)
       diamonds.remove(card)
       print(f"Your hand: {hand}", f"Remaining cards: {diamonds}", sep="\n")
       random.shuffle(diamonds) 

if not diamonds:
    print("There are no more cards to pick.")
    

