"""Components for the blackjack game"""

import random

# Special cards values.
a = 11
j = q = k = 10

# Deck of cards containing the 4 suits (pikes, hearts, clubs and diamonds)
COMPLETE_DECK = [a, 2, 3, 4, 5, 6, 7, 8, 9, 10, j, q, k] * 4  # Total of 52 cards


# Logo
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


# Deal cards
def deal(deck: list) -> int:
    """Deal one card and takes it out from the playing deck.
    Needs to import random module."""
    # Random number for using it as index.
    card_index = random.randint(0, len(deck) - 1)
    # Taking out the random card from the playing deck
    card = deck.pop(card_index)

    return card


# Calculate the sum of the cards
def calculate_score(turn: list) -> int:
    """Returns the sum of the total hand for a given player."""
    # BLACKJACK sum 21 with ONLY two cards
    if sum(turn) == 21 and len(turn) == 2:
        return 0

    # Change the value of the ACE to "1" if score is greater than 21
    if a in turn and sum(turn) > 21:
        turn.remove(a)
        turn.append(1)

    return sum(turn)


# Winner
def check_winner(user_score: int, computer_score: int) -> str:
    """Returns the winner of the hand."""
    if user_score > 21:
        return "You went over.\nYou lose, the bank wins."
    elif user_score == computer_score:
        return "It's a draw."
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif computer_score == 0:
        return "You lose. Dealer has a Blackjack."
    elif computer_score > 21:
        return "Dealer went over.\nYou win!"
    elif user_score > computer_score:
        return "You win"
    # If dealer's hand is bigger than user score
    else:
        return "You lose"