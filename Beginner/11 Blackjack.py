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
import random
import os


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def compare(user_score, computer_score):
    if user_score == computer_score:
        print("It's a draw")
    elif computer_score == 0:
        print("Computer has Blackjack. You lose.")
    elif user_score == 0:
        print("You have a Blackjack. You win!")
    elif user_score > 21:
        print(f"Your score is {user_score}. You lose.")
    elif computer_score > 21:
        print(f"Computer score is {computer_score}. You win!")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("You lose.")


def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer's first card: {computer_cards[0]}")
    while not is_game_over:
        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Do you want to draw another card? 'y' or 'n': ")
            if another_card == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"    Your cards: {user_cards}, current score: {user_score}")
            else:
                is_game_over = True

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    compare(user_score, computer_score)
    print(f"Computer's final hand: {computer_cards} and score: {computer_score}")
    new_game = input("Do you want to play again? 'y' or 'n': ")
    if new_game == "y":
        os.system("cls")
        blackjack()


blackjack()
