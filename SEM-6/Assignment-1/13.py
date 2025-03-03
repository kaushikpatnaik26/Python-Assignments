class InsufficientFundsError(Exception):
    def __init__(self, balance, withdrawal_amount):
        self.balance = balance
        self.withdrawal_amount = withdrawal_amount
    def __str__(self):
        return f"Insufficient funds! Current balance: {self.balance}, Withdrawal attempt: {self.withdrawal_amount}"
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        else:
            self.balance -= amount
            print(f"Withdrawal successful! Remaining balance: {self.balance}")

account = BankAccount(1200)
try:
    account.withdraw(1900)
except InsufficientFundsError as e:
    print(e)
    
