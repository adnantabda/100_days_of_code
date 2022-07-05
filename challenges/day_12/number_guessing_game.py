"""Number Guessing Game.
Project for Angela Wu's 100 days of code challenges.
Day # 12
"""

import random

def guessing_game():

    print("Welcome to the Number Guessing Game, my friend.")
    print("So... I heard you're saying you can guess what other people are thinking of...")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Let's see what are you made of!\n\n\n")
    difficulty = input("Select the difficulty level; enter 'easy' or 'hard': ").lower()

    while difficulty != "easy" and difficulty != "hard":
        difficulty = input("Select the difficulty level; enter 'EASY' or 'HARD': ").lower()

    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5


    print(f"Ok, so you chose level {difficulty}")
    number = random.randint(1, 100)
    print(f"Pssssssssttt, hint. The number is {number}")
    guess = input("Make a guess: ")

    while not guess.isdecimal():
        guess = input("That's not a valid number.\nMake a guess: ")

    while guess != number and attempts > 0:
        guess = int(guess)
        attempts -= 1

        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            continue
        print(f"Remaining attempts: {attempts}")
        guess = input("Make a guess: ")
        while not guess.isdecimal():
            guess = input("That's not a valid number.\nMake a guess: ")

    if guess == number and attempts >= 0:
        print("Congratulations, you've guessed my number.")
    else:
        print(f"You've lost!\nI was thinking of number {number}")


guessing_game()

while input("Do you want to play again? 'y' or 'n': ").lower() == 'y':
    guessing_game()
