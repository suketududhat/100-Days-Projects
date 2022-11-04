from art import logo, vs
from game_data import data
import random
import os


def person_picker():
    person = random.choice(data)
    name = person["name"]
    follower_count = person["follower_count"]
    description = person["description"]
    country = person["country"]
    attributes = f"{name}, a {description}, from {country}"
    return attributes, follower_count


def compare(followers_A, followers_B, user_input, user_score):
    if (followers_A <= followers_B or user_input != "A") and (
        followers_B <= followers_A or user_input != "B"
    ):
        return True, f"Sorry, that's wrong. Final score: {user_score}", user_score
    user_score += 1
    return False, f"You're right! Current score: {user_score}", user_score


is_game_over = False
attributes_A, followers_A = person_picker()
user_score = 0
message = ""
while not is_game_over:
    print(logo)
    print(message)
    print(f"Compare A: {attributes_A}")
    print(vs)
    attributes_B, followers_B = person_picker()
    print(f"Compare B: {attributes_B}")
    user_input = input("Who has more followers? Type 'A' or 'B': ")
    is_game_over, message, user_score = compare(
        followers_A, followers_B, user_input, user_score
    )
    attributes_A, followers_A = attributes_B, followers_B
    os.system("cls")
    if is_game_over:
        print(logo, message)
