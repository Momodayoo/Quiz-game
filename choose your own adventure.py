import random

# Description: A simple text-based adventure game where the player makes choices to navigate through the game.
name = input("What is thee name fellow adventurer? ")

def start_game():
    print("Welcome", name, "to the adventure game!")
    print("It was a good Friday night at the tavern. You remembered having a few drinks with the dwarves. And slowly the world around you turns dark...")
    print("You woke up with the rain drops falling on your face. Faint howlings of wolves echoes through the night. From afar you see a cave. Should you seek shelter or stay in the rain? (cave/rain)") 

    choice = input("> ")
    if choice.lower() == "cave":
        enter_cave()
    elif choice.lower() == "rain":
        print("You decide to stay outside. The wolves pack has surrounded you, thus your life is forfeitted.")
    else:
        print("Invalid choice. Please choose yes or no.")
        start_game()

def enter_cave():
    print("You are now inside the cave. You see two paths. Which one do you take? (left/right)")

    choice = input("> ")
    if choice.lower() == "left":
        left_path()
    elif choice.lower() == "right":
        right_path()
    else:
        print("Invalid choice. Please choose left or right.")
        enter_cave()

def left_path():
    print("You took the left path. You found a treasure chest!")

    choice = input("Do you want to open it? (yes/no) ")
    if choice.lower() == "yes":
        found_treasure()
    elif choice.lower() == "no":
        print("You decide to leave the treasure chest. Game Over.")
    else:
        print("Invalid choice. Please choose yes or no.")
        left_path()

def found_treasure():
    print("You found a treasure chest! You win 100 coins!")
    coins = 100
    print("You now have", coins, "coins. Congratulations!")
    
    choice = input ("Do you want to take the other path? (yes/no)")

    if choice.lower() == "yes":
        right_path()
    elif choice.lower() == "no":
        print("Well, there's no other way than to go except the other path")
        right_path()

def right_path():
    print("You took the right path. You encountered a monster! ")
    choice = input ("What do you do? (fight/run)")

    if choice.lower() == "fight":
        print ("Roll greater than 10 to win the fight!")

        def roll_dice():
            return random.randint(1, 20)
        print ("You rolled a", roll_dice())
        if roll_dice() > 10 < 20:
            print("You won the fight and retrieved the monster's horn! You decide to make a mug out of it as memento and went home! Congratulations!")
        else:
            print("You lost the fight. The Monster tore apart your limbs. Game over")
    elif choice.lower() == "run":
        print("You decide to run away from the monster. You trip on a rock and the monster catches you. Game Over.")
start_game()

# continue making your own game storylines and choices!