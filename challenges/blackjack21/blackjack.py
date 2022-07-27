"""Blackjack - 21.
Project for Angela Wu's 100 days of code challenges.
Day # 11
"""
from components import *


def blackjack():
    """A single player blackjack game."""
    # Copy of the complete deck to remove the cards already out
    game_deck = COMPLETE_DECK[:]
    print(len(game_deck))
    # Players start with an empty hand
    player_cards = []
    dealer_cards = []

    # Dealing the first 2 cards of the starting game
    for _ in range(2):
        player_cards.append(deal(game_deck))
        dealer_cards.append(deal(game_deck))

    # Player's  turn
    game_over = False
    while not game_over:
        # Calculate score on each card drawn
        player_score = calculate_score(turn=player_cards)
        dealer_score = calculate_score(turn=dealer_cards)
        # Print the player's hand and total and only the dealer's FIRST CARD
        print(f"\n\tYour hand: {player_cards}\n\tYour total: {player_score}")
        print(f"\tDealer's hand: {[dealer_cards[0], 'X']}")

        # Check for a blackjack or if the player went over of 21
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:  # Game continues. Ask the player to choose hit or stand
            if input("\nEnter 'h' to hit another card or 's' to stand: ").lower() == 'h':
                player_cards.append(deal(game_deck))
            else:  # User doesn't want another card
                game_over = True

    # Dealer's turn
    if player_score <= 21:

        # Reveal the 2 cards of the dealer
        print(f"\n\tDealer's hand: {dealer_cards}\n\tDealer total: {dealer_score}")

        while dealer_score < 17 and dealer_score != 0:
            dealer_cards.append(deal(game_deck))
            dealer_score = calculate_score(dealer_cards)
        print("\nFinal scores:")
        print(f"\tYour hand: {player_cards}\n\t\tTotal: {player_score}")
        print(f"\tDealer's hand: {dealer_cards}\n\t\tTotal: {dealer_score}\n")

    # Inform winner
    print(check_winner(user_score=player_score, computer_score=dealer_score))


while input("\nDo you want to play a game of Blackjack?\nEnter 'yes' or 'no'. ").lower() == 'yes':
    blackjack()
