import random


pips = random.randint(1,6)
print("pip numb is",pips, "pip me")

prizes = ["car","$1000","a mule","trip to mexico"]
prize_won = print(f"You won: {random.choice(prizes)}")

print(prizes[0])
random.shuffle(prizes)
print(prizes[0])

cards =  [1,2,3,4,5,6,7,8,9,10,11]
random.shuffle(cards)
print(cards)
 