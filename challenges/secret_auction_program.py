"""
Secret Auction Program.
Project for Angela Wu's 100 days of code challenges.
"""

# Logo
logo = """
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
"""


def find_high_bid(bids_participants: dict):
    """Find the highest bidder from a dict. containing the name and the bid."""
    highest_bid = 0
    highest_bidder = ''
    for bidder in bids_participants:
        bid = bids_participants[bidder]
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = bidder

    print(f"The winner is {highest_bidder}, with a bid of ${highest_bid}")


def bidders() -> dict:
    """Returning bidders as a dict."""
    participants = {}
    # Flag
    new_bid = True
    while new_bid:
        bidder = input("Enter your name:\n")
        bid = float(input("Enter your bid:\n$"))
        participants[bidder] = bid
        # Adding more bidders
        more_bids = input("Want to add another bidder? [y / n]\n").lower()
        if more_bids == 'n':
            new_bid = False
        # Clear screen so next bidder won't see previous bid
        print("\n" * 50)
    # Returns a dict
    return participants


# Title
print("The Secret Auction Program\n\n")
print(logo)
print("\n\n\n\n")
print("Let's start adding the bidders")

bids = bidders()
find_high_bid(bids)
