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

# Contains strings detailing the cpu/ player's ending state
end_states = {
    "won": "Won!",
    "blackjack": "Blackjack!",
    "lost": "Lost!",
    "bust": "Bust!",
    "push": "Push!",
    "blackjacks": "Blackjack! -> Push!"
}

# Contains messages indicating the game'a final result based
# based on the player's ending state
end_msgs = {
    "won": "You won!",
    "blackjack": "You won!",
    "lost": "You lost!",
    "bust": "You lost!",
    "push": "You tied!",
    "blackjacks": "You tied!"
}
