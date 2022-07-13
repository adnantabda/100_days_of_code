"""Higher Lower Game.
Project for Angela Wu's 100 days of code challenges.
Day # 14
"""
import random

from game_data import data
from ascii_art import logo, vs


def check_values(value_1: dict, value_2: dict, source: list) -> dict:
    """Change second value if are iqual, and returns a new random value from source."""
    while value_1 == value_2:
        value_2 = random.choice(source)
    return value_2


def higher_lower():
    """Game where you have to guess who has more followers."""
    score = 0  # Initial score
    option_a = random.choice(data)  # Setting initial value
    win = True
    while win:
        option_b = random.choice(data)
        print(logo)
        print(f"\nCompare A:\n\t{option_a['name']}, "
              f"{option_a['description']}"
              f" from {option_a['country']}"
              )
        print(vs)
        print(f"Against B:\n\t{option_b['name']}, "
              f"{option_b['description']}"
              f" from {option_b['country']}"
              )
        answer = input("\nWho has more followers?\nType 'A' or 'B': ").lower()

        if answer == 'a':
            answer = option_a
            vs_followers = option_b["follower_count"]  # Returns number of followers
        else:
            answer = option_b
            vs_followers = option_a["follower_count"]

        if answer['follower_count'] >= vs_followers:
            score += 1
            print(f"Correct!\nCurrent Score : {score}")
            option_a = answer  # To compare vs new option_b on top of while loop
        else:
            win = False
            print(f"\n\nSorry, you've lost.\nFinal score: {score}")
            # Play again?
            if input("Do you want to play again?\n['y'/'n']: ").lower() == 'y':
                higher_lower()


higher_lower()
