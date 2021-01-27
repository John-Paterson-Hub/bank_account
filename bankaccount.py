class BankAccount:
    def __init__(self):
        self.int_rate = .10
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        self.yield_interest()
        return self

    def withdraw(self, amount):
        self.balance -= amount
        self.yield_interest()
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance} intrest rate: {self.int_rate}")

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

Tom = BankAccount()

Tom.deposit(100).display_account_info()