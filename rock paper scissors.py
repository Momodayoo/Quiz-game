import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose either 'rock', 'paper', or 'scissors'.")

    user_choice = input()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f"The computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print("You win!")
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("You win!")
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print("You win!")
    else:
        print("You lose!")

rock_paper_scissors()   # Call the function

# Path: rock%20paper%20scissors.py

while True:
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        rock_paper_scissors()
    else:
        print("Thanks for playing!")
        break

