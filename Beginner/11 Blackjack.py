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
import os
import random
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_cards = []
computer_score = 0
while computer_score < 17:
    computer_cards.append(cards[random.randint(0, 12)])
    computer_score = sum(computer_cards)

player_cards = []
player_score = 0
player_cards.append(cards[random.randint(0, 12)])
player_cards.append(cards[random.randint(0, 12)])

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play_game == "y":
    # os.system("cls")
    print(logo)
    
    player_score = sum(player_cards) 
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(computer_cards)
    print(f"Computer's first card: {computer_cards[0]}")
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == "y":
        player_cards.append(cards[random.randint(0, 12)])

else:
    os.system("cls")
    exit

