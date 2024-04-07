import random

random.randrange(1, 101) # Generates a random number between 1 and 100

def guess_number():
    number = random.randint(1, 100)
    guess = 0
    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
    print("You got it!")

guess_number()

# Path: number%20guesser.py



