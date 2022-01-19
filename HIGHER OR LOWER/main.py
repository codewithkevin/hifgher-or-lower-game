import random
from game import GameBrain
from game_data import data
from account import Account

generating = []
for account in data:
    account_name = account['name']
    account_followers = account['follower_count']
    account_des = account['description']
    account_country = account['country']
    new = Account(account_name, account_followers, account_des, account_country)
    generating.append(new)

guess = ""

user_account = random.choice(generating)
computer_account = random.choice(generating)

"""Getting followers in the two user account"""

game = GameBrain(user_account, computer_account, guess)

account_followers = user_account['follower_count']
account_b_followers = computer_account['follower_count']
print(account_followers)
print(account_b_followers)

is_on = True


while is_on:
    game.compare()
    is_correct = game.check_answer(account_followers, account_b_followers)

    if is_correct:
        print(f"You had it right")
        print()
    else:
        print("You had it wrong")


