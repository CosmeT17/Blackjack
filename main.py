# Blackjack
from blackjack import play_blackjack
play_blackjack()



# FOR TESTING ---------------------------------------------------------------------
# Blackjack - A total of 21 with only the first two cards dealt 

# Win:
#   * Player gets a blackjack and cpu doesn't, no need for the cpu to draw. ✔ 
#   * The player's legal total is greater than the cpu's legal total. ✔ 
#   * The cpu's total went over 21 - only possible if the player's didn't. ✔
#
# Lose:
#   * The cpu got a blackjack and the player did't. ✔ 
#   * The player's total went over 21, no need for the cpu to draw. ✔
#   * The cpu's legal total is greater than the player's legal total. ✔
#
# Tie:
#   * The player's and cpu's totals are equal ✔
#   * Two blackjacks count as a tie ✔
#   * When a blackjack and non-blackjack 21 are present, the blackjack wins. ✔
#
#
# CPU draws in push? Yes ✔
# CPU draws when player get's blackjack? No ✔
# CPU draws when player get's bust? No ✔
# ---------------------------------------------------------------------------------
