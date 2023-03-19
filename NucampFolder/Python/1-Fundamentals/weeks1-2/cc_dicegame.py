import random

high_score = 0


def dice_game():
    high_score = 0
    while True:
        
        print("\nCurrent High Score:", high_score)
        print("1) Roll Dice \n2) Leave Game")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            dice_one = random.randint(1,12)
            dice_two = random.randint(1,12)
            print("\nYou roll a...", dice_one)
            print("You roll a...", dice_two)
            score = dice_one + dice_two
            print("\nYou have rolled a total of:", score)
            if high_score < score :
                high_score = score
                print("\nNew high score!")
        if choice == 2:
            print("Goodbye!")
            break




dice_game()
