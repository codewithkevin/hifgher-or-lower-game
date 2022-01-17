import random


class GameBrain:

    def __init__(self, account, account_b, choice):
        self.account = account
        self.account_b = account_b
        self.choice = choice

    def compare(self):
        if self.account == self.account_b:
            self.account_b = random.choice(self.account_b)
        print(f"A: {self.account}")
        print('VS')
        print(f"B: {self.account_b}")
        print()

        self.choice = input("Which Account has more followers, A or B:\n")

    def check_answer(self, a_followers, b_followers):
        var_a = self.choice = 'a'
        var_b = self.choice = 'b'

        if var_a:
            if a_followers > b_followers:
                return True
            return False

        elif var_b:
            if b_followers > a_followers:
                return True
            return False
