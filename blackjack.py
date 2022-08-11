# Contains the code for playing a game of blackjack

from io_handling import get_keypress, clear_line, move_cursor, clear_lines
from art import LOGO, DEAL_PROMPT, OPTION_BOXES, end_states, end_msgs
from random import choices

# Ace starts out as 11/ K, Q, and J equal to 10
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

# Calculates the total for the given hand of cards
def calculate_total(hand):
    '''Calculates the total for the given hand of cards.
    
    Will automatically convert the value of an Ace to the
    most advantageous value.'''
    
    # Calculating the total
    total = sum(hand)

    # If an ace is present, pick the best possible combination
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total -= 10
    
    return total

def play_blackjack():
    "Plays a game of blackjack when called."
    
    # Printing the logo
    print(LOGO)

    # Asking the player if they want to deal the next two cards
    keypress = get_keypress(DEAL_PROMPT, ['Y', 'N']) 
    while keypress != 'N':
        # Contains the player's/ cpu's ending state
        player_end_state = 'lost'
        cpu_end_state = 'won'
    
        # The player chose YES - clear the deal prompt
        clear_line(len(DEAL_PROMPT))
        
        # Dealing two cards for the player and cpu hands
        player_hand = choices(deck, k = 2)
        cpu_hand = choices(deck, k = 2)
    
        # Calculating the total for the player and cpu hands
        player_total = calculate_total(player_hand)
        cpu_total = calculate_total(cpu_hand)

        # The cpu got a BLACKJACK
        if cpu_total == 21: cpu_end_state = "blackjack"
        
        # Creating the card strings for printing
        player_cards = str(player_hand)
        cpu_cards = f"[?, {cpu_hand[1]}]"
        max_len = max(len(player_cards), len(cpu_cards)) # Used for spacing
        
        # Printing the player and cpu card strings with the total
        print(f"          Your Cards:    {player_cards.ljust(max_len)}  ({player_total})")
        print(f"    Computer's Cards:    {cpu_cards.ljust(max_len)}  ({cpu_hand[1]})\n")
    
        # Checking if the player does not already have a BLACKJACK
        if player_total != 21:
            # Asking the player if they want to hit or stand
            keypress = get_keypress(OPTION_BOXES + '\n', ['Y', 'N'])
    
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
                    player_end_state = "bust"
                    break
                # The player's total is 21
                elif player_total == 21: break
                
                # Getting the next keypress
                keypress = get_keypress('', ['Y', 'N'])
    
            # Clear the OPTION_BOXES from the screen 
            clear_lines(38, 4, False)
            
            # Updating the dealer's cards and total if needed
            if player_end_state != "bust":
                while cpu_total < 17:
                    cpu_hand.extend(choices(deck))
                    cpu_total = calculate_total(cpu_hand)
        
                # Checking whether the cpu lost or tied    
                if cpu_total > 21: 
                    cpu_end_state = "bust"
                    player_end_state = "won"
                elif cpu_total < player_total:
                    cpu_end_state = "lost"
                    player_end_state = "won"
                elif cpu_total == player_total: cpu_end_state = player_end_state = "push" 
            
        # The player was dealt a BLACKJACK
        else: 
            # The cpu was also dealt a blackjack - tie
            if cpu_end_state == "blackjack": player_end_state = cpu_end_state = "blackjacks"
            
            # Player wins with a blackjack
            else:
                player_end_state = "blackjack"
                cpu_end_state = "lost"
            
        # Revealing the cpu's cards/ editing spacing for totals/
        # printing the cpu & player ending messages
        cpu_cards = str(cpu_hand)
        max_len = max(len(player_cards), len(cpu_cards)) # Used for spacing
        move_cursor(25 + len(player_cards), 3)
        space = ' ' if len(str(player_total)) < len(str(cpu_total)) else '' # Used for spacing
        print((max_len - len(player_cards)) * ' ' + f"  ({player_total}){space}", end = '')
        print(f"    {end_states[player_end_state]}")
        move_cursor(25, 0)
        if len(str(player_total)) != len(str(cpu_total)): # Used for spacing
            if space == '': space = ' '
            else: space = ''
        print(f"{cpu_cards}" + (max_len - len(cpu_cards)) * ' ' + f"  ({cpu_total}){space}", end = '')
        print(f"    {end_states[cpu_end_state]}\n")
    
        # Printing the game's final result
        print(end_msgs[player_end_state], '\n')

        # Asking the player if they want to play again
        keypress = get_keypress(DEAL_PROMPT, ['Y', 'N'])

        # Clearing the screen of the current game
        clear_lines(100, 6)

    # The player chose not to deal - end the game
    else:
        clear_line(len(DEAL_PROMPT))
        print("GOOD BYE!")
