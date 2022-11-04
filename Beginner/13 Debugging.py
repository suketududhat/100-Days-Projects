###########DEBUGGING#####################

# Describe Problem
def my_function():
    for i in range(1, 20):
        if i == 20:  # 20 will never be reached in this range
            print("You got it")


my_function()

# Reproduce the Bug
from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)  # list index is 0 to 6
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:  # 1994 won't evaluate, so one of the criteria needs to be adjusted
    print("You are a Gen Z.")

# Fix the Errors
age = input("How old are you?")  # needs an int() conversion
if age > 18:
    print("You can drive at age {age}.")  # 1 indent and f string

# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))  # == instead of =
total_words = pages * word_per_page
print(total_words)

# Use a Debugger
def mutate(a_list):  # sourcery skip: merge-list-append, move-assign-in-block
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)  # Needs 1 more indent
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
