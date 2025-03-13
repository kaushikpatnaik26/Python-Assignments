
class InsufficientBalance(Exception):
    def __init__(self, balance, withdrawal_amount):
        self.balance = balance
        self.withdrawal_amount = withdrawal_amount
        super().__init__(f"Insufficient balance! Available: {balance}, Requested: {withdrawal_amount}")

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}")
        else:
            raise ValueError("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalance(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}")

account = BankAccount(100)

account.deposit(50)

try:
    account.withdraw(120)
except InsufficientBalance as e:
    print(f"Error: {e}")

account.withdraw(80)

try:
    account.withdraw(100)
except InsufficientBalance as e:
    print(f"Error: {e}")
