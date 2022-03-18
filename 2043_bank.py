"""
2043. 简易银行系统
"""


class Bank:

    def __init__(self, balance):
        self.balance = balance

    def check_account(self, account):
        if account > len(self.balance) or account < 1:
            return False
        else:
            return True

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.check_account(account1) or not self.check_account(account2):
            return False

        if self.balance[account1 - 1] - money >= 0:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if not self.check_account(account):
            return False

        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.check_account(account):
            return False

        if self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        else:
            return False
