# Blackjack
from io_handling import get_keypress, clear_line, move_cursor, clear_lines
from art import LOGO, DEAL_PROMPT, OPTION_BOXES
from random import choices

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

# BOOLEANS
bust = False
    
# Printing the logo
print(LOGO)

# Asking the player if they want to deal the next two cards
if get_keypress(DEAL_PROMPT, ['Y', 'N', '\r']) != 'N':
    # The player chose YES - clear the deal prompt
    clear_line(len(DEAL_PROMPT))
    
    # Dealing two cards for the player and cpu hands
    player_hand = choices(deck, k = 2)
    cpu_hand = choices(deck, k = 2)

    # Calculating the total for the player and cpu hands
    player_total = calculate_total(player_hand)
    cpu_total = calculate_total(cpu_hand)
    
    # Creating the card strings for printing
    player_cards = str(player_hand)
    cpu_cards = f"[?, {cpu_hand[1]}]"
    max_len = max(len(player_cards), len(cpu_cards)) # Used for spacing
    
    # Printing the player and cpu card strings with the total
    print(f"          Your Cards:    {player_cards.ljust(max_len)}  ({player_total})")
    print(f"    Computer's Cards:    {cpu_cards.ljust(max_len)}  ({cpu_hand[1]})\n")

    # TESTING ----------------------------------------------------------------------------
    # print(f"\tTESTING: {cpu_hand}  ({cpu_total})\n")
    # ------------------------------------------------------------------------------------

    # Checking if the player does not already have a BLACKJACK
    if player_total != 21:
        # Asking the player if they want to hit or stand
        keypress = get_keypress(OPTION_BOXES + '\n', ['Y', 'N', '\r'])

        # Player chose hit
        while keypress != 'N':
            # Adding a card to the players hand and printing the results
            move_cursor(25, 7)
            player_hand.extend(choices(deck))
            player_total = calculate_total(player_hand)
            player_cards = str(player_hand)
            print(f"{player_cards}  ({player_total})")
    
            # Moving the cpu_total to be in line with the player_total
            move_cursor(25 + len(cpu_cards), 0)
            print(' ' * (len(player_cards) - len(cpu_cards)) + f"  ({cpu_hand[1]})")
            move_cursor(0, -5)
    
            # The player's total is now greater than 21 - BUST
            if player_total > 21:
                bust = True
                break
            # The player's total is 21 - BLACKJACK
            elif player_total == 21: break
            
            # Getting the next keypress
            keypress = get_keypress('', ['Y', 'N', '\r'])

        # Clear the OPTION_BOXES from the screen 
        clear_lines(38, 4)
        
    # The player was dealt a BLACKJACK
    else: pass
            
    # Updating the dealer's cards and total
    if not bust: 
        while cpu_total < 17:
            cpu_hand.extend(choices(deck))
            cpu_total = calculate_total(cpu_hand)
    cpu_cards = str(cpu_hand)
    max_len = max(len(player_cards), len(cpu_cards)) # Used for spacing
    
    # Revealing the computer's cards/ editing spacing for totals
    move_cursor(25 + len(player_cards), 3)
    print((max_len - len(player_cards)) * ' ' + f"  ({player_total})")
    move_cursor(25, 0)
    print(f"{cpu_cards}" + (max_len - len(cpu_cards)) * ' ' + f"  ({cpu_total})\n")

    # Check win/ lose conditions
    # Print results
        
# The player chose not to deal - end the game
else:
    clear_line(len(DEAL_PROMPT))
    print("GOOD BYE!")

# TO DO:
#   1. Create deck of cards ✔️
#     * List with 12 card options ✔️
#   2. Add deal option
#     * Ask if the player wants to deal ✔️
#     * Deal two cards for the player ✔️
#     * Deal two cards for the CPU ✔️
#     * Show cards and calculate total - SPECIAL for ACE✔️

#   3. Add hit or stand option
#     * Player can press hit until the total is greater than or equal to 21 ✔️
#     * Player has the ability to press stand ✔️
#     * CPU must hit while they have 16 or lower ✔️
#     * Dealer does not hit if player gets bust ✔️
#     * Reveal the CPU's cards ✔️

#   4. Calculate win or loss

#   5. Add replayability
#   6. Clean up code
