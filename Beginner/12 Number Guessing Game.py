import random

logo = """
 _______               ___.                    ________                            .__                
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  >
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  / 
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/  
"""

random_number = random.randint(1, 100)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Correct answer is {random_number}")
difficulty = input("Choose a difficulty - 'easy' or 'hard': ")
guess_remaining = 10 if difficulty == "easy" else 5
while guess_remaining > 0:
    print(f"You have {guess_remaining} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess == random_number:
        print(f"You got it! The answer was {random_number}")
        guess_remaining = -1
    elif user_guess < random_number:
        print("Too low.")
        guess_remaining -= 1
    else:
        print("Too high.")
        guess_remaining -= 1

    if guess_remaining == 0:
        print("You've run out of guesses, you lose.")
