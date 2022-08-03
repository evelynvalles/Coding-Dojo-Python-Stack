class BankAccount:
    # don't forget to add some default values for these parameters!

    def __init__(self, int_rate, balance = 0): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        # your code here
        self.balance = self.balance + amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        # your code here
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
            # print(self.balance)
        else:
            self.balance = self.balance - amount
            print(self.balance)
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

class User:
    def __init__(self, name, email, bank_account):
        self.name = name
        self.email = email
        self.account = bank_account
    
    # other methods
    
    def make_deposit(self, amount):
    	# your code here
        self.account.deposit(amount)

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        self.account.display_account_info()

account1 = BankAccount(0.01, 500)
user1 = User('Evelyn', 'ev@gmail.com', account1)

user1.make_deposit(100)
user1.make_withdrawl(50)
user1.display_user_balance()
