from random import choice

print("*** Welcome to Blackjack ***")

deck = ["A", "1", "2"]
card = choice(deck)


print("         _______ ") 
print(f"       |{card} |")
print("        |       |")
print("        |       |")
print(f"       |_{card}|")