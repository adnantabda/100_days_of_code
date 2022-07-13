""" The Hangman Game.
Project for Angela Wu's 100 days of code challenges.
Day # 7
"""

import random
import sys


import components

# Title
print(components.logo)

# Chose a random word from components/word_list
chosen_word = random.choice(components.word_list)

# Generate the blanks of the word
display_word = ["_"] * len(chosen_word)
# Guessing chances
lives = 6
# Chosen letters
chosen_letters = []

print("Word:")
print(f'\t\t{" ".join(display_word)}')

# Repeat till there are no more blanks to display or lose all lives
while "_" in display_word and lives > 0:
    print("\n(Type 'quit' to exit the game)")
    guess = input("Guess a letter: ").lower()

    # To clear screen (on linux)
    # os.system("clear")

    # To clar screen on windows; os.system("cls")

    # Quit game
    if guess == "quit":
        print("Good bye.")
        sys.exit()

    # Check user not to enter more than 1 LETTER
    while len(guess) != 1 or not guess.isalpha():
        print("\nI said A letter!\n")
        guess = input("Guess a letter: ").lower()

    # Already chosen that letter
    if guess in chosen_letters:
        print(f"You've already chosen letter: '{guess}'.\nYou loose a life\n")
        lives -= 1
    # Guessed letter match a letter in word
    elif guess in chosen_word:
        chosen_letters.append(guess)
        print("\nCorrect!")
        # Obtain the index of each letter
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                # Change the blank for the letter
                display_word[index] = letter
    # No match. Loose a life
    else:
        print(f"\nNope, you loose a life!")
        chosen_letters.append(guess)
        lives -= 1

    if lives == 1:
        print("Last chance! Good luck!")

    # Display the word with it's blanks and remaining lives
    print(components.stages[lives])
    print(f"Chosen letters: {' - '.join(chosen_letters)}")
    print(f"Remaining lives: {lives}")
    print(f"\nWord:\n\t\t{' '.join(display_word)}")


# End game
print("\n\n\n\nGAME OVER")
print(components.stages[lives])
if lives == 0:
    print("YOU'VE LOST")
    print(f"The word was: {chosen_word}")
else:
    print("YOU WIN!!!")

