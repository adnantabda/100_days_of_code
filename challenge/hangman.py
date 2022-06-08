"""
The Hangman.
Project for Angela Wu's 100 days of code challenge.
Day # 7
"""

import random
import sys

# Title
print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                
"""
      )

# TODO use a file or api to get random words
word_list = ["aardvark", "baboon", "camel"]

# Chose a random word from word_list
chosen_word = random.choice(word_list)

# Generate the blanks of the word
display_word = ["_"] * len(chosen_word)
# Guessing chances
lives = 6

print("Word:")
print(f'\t\t{" ".join(display_word)}')

# Repeat till there are no more blanks to display or lose all lives
while "_" in display_word and lives > 0:
    print("\n(Type 'quit' to exit the game)")
    guess = input("Guess a letter: ").lower()

    # Quit game
    if guess == "quit":
        print("Good bye.")
        sys.exit()

    # Check user not to enter more than 1 LETTER
    while len(guess) != 1 or not guess.isalpha():
        print("I said A letter!")
        guess = input("\nGuess a letter: ").lower()

    # Guessed letter match a letter in word
    if guess in chosen_word:
        print("Correct!")
        # Obtain the index of each letter
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                # Change the blank for the letter
                display_word[index] = letter

    # No match. Loose a life
    else:
        print(f"You loose a life.")
        lives -= 1
        if lives == 1:
            print("Last chance! Good luck!")

    # Display the word with it's blanks and remaining lives
    print("\n" + " ".join(display_word))
    print(f"\nRemaining lives: {lives}")

# End game
print("\nGAME OVER")
if lives == 0:
    print("YOU'VE LOST")
    print(f"The word was: {chosen_word}")
else:
    print("YOU WIN!!!")

