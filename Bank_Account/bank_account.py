class BankAccount:
    # don't forget to add some default values for these parameters!
    all_BankAccounts = []

    def __init__(self, int_rate, balance = 0): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_BankAccounts.append(self)
        # don't worry about user info here; we'll involve the User class soon

    @classmethod
    def print_bank_instances(cls):
        for all_bank_accounts in cls.all_BankAccounts:
            print(f"Balance: {all_bank_accounts.balance}")

    def deposit(self, amount):
        # your code here
        self.balance = self.balance + amount
        # print(self.balance)
        return self

    def withdraw(self, amount):
        # your code here
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
            # print(self.balance)
        else:
            self.balance = self.balance - amount
            # print(self.balance)
        return self

    def display_account_info(self):
        # your code here
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance = self.balance * self.int_rate + self.balance
            # print(self.balance)
        else: 
            False
        return self

    def __repr__(self):
        return f"Bank Account Object Name:{self.balance}"


account1 = BankAccount(0.01,200)
account2 = BankAccount(0.05,500)

account1.deposit(100).deposit(200).deposit(500).withdraw(200).yield_interest().display_account_info()
account2.deposit(500).deposit(1000).withdraw(100).withdraw(200).withdraw(50).withdraw(100).yield_interest().display_account_info()

BankAccount.print_bank_instances()

