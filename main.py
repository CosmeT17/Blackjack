# Blackjack
from readchar import readkey
from random import choices
# from replit import clear

# Ace starts out as 11/ K, Q, and J equal to 10
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

# Calculates the total for the given hand of cards
def calculate_total(hand):
    # Calculating the total
    total = sum(hand)

    # If an ace is present, pick the best possible combination
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total -= 10
    
    return total

while True:
    # Asking the player if they want to deal the next two cards
    print("Deal the next cards (Y/N)?", end = '', flush = True)
    keypress = readkey().upper()
    while keypress not in ['Y', 'N', '\r']: keypress = readkey().upper()
    
    if keypress != 'N':
        # Dealing two cards for the player and cpu hands
        player_hand = choices(deck, k = 2)
        cpu_hand = choices(deck, k = 2)

        # Creating the card strings for printing, max_len is used for spacing
        player_cards = str(player_hand)
        cpu_cards = f"[?, {cpu_hand[1]}]"
        max_len = max(len(player_cards), len(cpu_cards))

        # Calculating the total for the player and cpu hands
        player_total = calculate_total(player_hand)
        cpu_total = calculate_total(cpu_hand)

        # Printing the player and cpu cards
        print(f"\n\n\t      Your Cards:    {player_cards.ljust(max_len)}  ({player_total})")
        print(f"\tComputer's Cards:    {cpu_cards.ljust(max_len)}  ({cpu_hand[1]})\n")

        # TESTING ----------------------------------------------------------------------------
        print(f"\tTESTING: {cpu_hand}  ({cpu_total})\n")
        # ------------------------------------------------------------------------------------
    else: break

# TO DO:
#   1. Create deck of cards ✔️
#     * List with 12 card options ✔️
#   2. Add deal option
#     * Ask if the player wants to deal ✔️
#     * Deal two cards for the player ✔️
#     * Deal two cards for the CPU ✔️
#     * Show cards and calculate total - SPECIAL for ACE✔️

#   3. Add hit or stand option
#     * Player can press hit until the total is greater than 21
#     * Player has the ability to press stand
#     * CPU must hit while they have 16 or lower
#     * Reveal the CPU's cards

#   4. Calculate win or loss
