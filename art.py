# Contains all of the art used in the blackjack file

DEAL_PROMPT = "Deal the next cards (Y/N)?"

LOGO = '''.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
'''

OPTION_BOXES = '''\t -----------          ----------- 
\t|    HIT    |        |   STAND   |
\t|    (Y)    |        |    (N)    |
\t -----------          ----------- '''

end_messages = {
    # Player wins
    "PLAYER_BLACKJACK": "You got a BLACKJACK!\nYou Win!",
    "WIN": "Your total is greater than the computer's.\nYou Win!",
    "CPU_BUST": "CPU BUST: Computer's total went over 21.\nYou Win!",

    # Player loses
    "CPU_BLACKJACK": "The computer got a BLACKJACK!\nYou Lose!",
    "PLAYER_BUST": "BUST: Your total went over 21.\nYou Lose!",
    "LOSS": "The computer's total is greater.\nYou Lose!",

    # Player ties
    "TIE": "PUSH: Your total is the same as the computer's.\nYou Tie!"
}
