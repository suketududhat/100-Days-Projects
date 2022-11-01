logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

import os

print(logo)
print('Welcome to the secret auction program.')

more_bids = True
bidder_log = []

while more_bids:
    username = input('What is your name? ')
    user_bid = int(input('What is your bid?: $'))
    other_bidders = input('Are there any other bidders? Type yes or no. ')
    bidder_log += [{"name": username, "bid": user_bid}]
    if other_bidders == 'no':
        more_bids = False
    else:
        os.system('cls')


max_bid = 0
for bidder in bidder_log:
    if bidder['bid'] > max_bid:
        max_bid = bidder['bid']
        max_bidder = bidder['name']

print(f"The winner is {max_bidder} with a bid of ${max_bid}!")