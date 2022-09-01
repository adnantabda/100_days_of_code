"""Number Guessing Game.
Project for Angela Wu's 100 days of code challenges.
"""
import random

title = """
╔╗╔┬ ┬┌┬┐┌┐ ┌─┐┬─┐  ╔═╗┬ ┬┌─┐┌─┐┌─┐┬┌┐┌┌─┐  ╔═╗┌─┐┌┬┐┌─┐
║║║│ ││││├┴┐├┤ ├┬┘  ║ ╦│ │├┤ └─┐└─┐│││││ ┬  ║ ╦├─┤│││├┤ 
╝╚╝└─┘┴ ┴└─┘└─┘┴└─  ╚═╝└─┘└─┘└─┘└─┘┴┘└┘└─┘  ╚═╝┴ ┴┴ ┴└─┘
"""


def select_level():
    """Choose what level you want to play."""
    difficulty = input("Select the difficulty level; enter 'easy' or 'hard': ").lower()
    while difficulty != "easy" and difficulty != "hard":
        difficulty = input("Not a valid level. Enter 'EASY' or 'HARD': ").lower()
    return difficulty


def guess_number():
    """Try to guess the number."""
    number = input("Make a guess: ")
    while not number.isdecimal():  # make sure it will be a valid number
        number = input("That's not a valid number.\nMake a guess: ")
    number = int(number)
    return number


def guessing_game():
    """Game where you hace to guess a number between 1 and 100."""
    print("\nI'm thinking of a number between 1 and 100.")
    print("Let's see what are you made of!\n\n")

    level = select_level()
    if level == "easy":
        attempts = 10
    else:  # Hard
        attempts = 5
    print(f"\nOk, so you chose level {level}. You'll have {attempts} attempts.")

    number = random.randint(1, 100)
    guess = guess_number()

    while guess != number and attempts > 1:
        attempts -= 1  # loose a life
        if guess < number:
            print("Too low.")
        if guess > number:
            print("Too high.")
        print(f"\nRemaining attempts: {attempts}")
        guess = guess_number()
    if guess == number and attempts >= 0:  # User wins
        print("\nCongratulations, you've guessed my number.")
    else:  # User lost
        print(f"\nYou've lost!\nI was thinking of number {number}")


###################################################################


print(title)
print("Welcome to the Number Guessing Game, my friend.")
print("So... I heard you're saying you can guess what other people are thinking of...")

guessing_game()
# Repeat
while input("\n\nDo you want to play again? 'y' or 'n': ").lower() == 'y':
    guessing_game()
