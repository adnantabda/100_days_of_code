"""
Rock-paper-scissors game.
Project for Angela Wu's 100 days of code challenge.
Day # 4
"""

import sys
import random

# Ascii art
rock = """
rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
paper!
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
scissors!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


# Game's functions
def menu():
    """Options menu with instructions."""
    print("\n\nChoose your move:")
    instructions = """
    [0] for ROCK.
    [1] for PAPER.
    [2] for SCISSORS.
    
    [q] for QUIT.
    """
    print(instructions)


def rps_game():
    """Game logic"""
    computer_choice = random.randint(0, 2)
    user_choice = input()
    # Flag
    valid = False

    while valid is False:
        # Quit game
        if user_choice == 'q':
            print("Bye!")
            sys.exit()

        else:
            try:
                user_choice = int(user_choice)
                # Validate range of answer
                if user_choice < 0 or user_choice > 2:
                    print("Wrong answer")
                    menu()
                    user_choice = input()
                else:
                    valid = True

            except ValueError:
                print("Invalid choice. You lose!")
                sys.exit()

    print(f"You chose {game_images[user_choice]}")
    print(f"Computer chooses {game_images[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw.")
        repeat()
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
        repeat()
    elif computer_choice == 0 and user_choice == 2:
        print("You lose! :(")
        repeat()
    elif user_choice > computer_choice:
        print("You win!")
        repeat()
    else:
        print("You lose! :(")
        repeat()


def repeat():
    """Play again menu."""
    print("\nDo you want to play again?")
    print("[y]es or [n]o:")
    play_again = input()

    if play_again == 'y':
        menu()
        rps_game()
    elif play_again == 'n':
        print("Bye!")
        sys.exit()
    else:
        while play_again != 'y' or play_again != 'n':
            print("[y]es or [n]o:")
            play_again = input()


print("ROCK, PAPER SCISSORS GAME:")
game_images = (rock, paper, scissors)

menu()
rps_game()









































