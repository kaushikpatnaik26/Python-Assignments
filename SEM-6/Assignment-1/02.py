class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs: {amount:.2f}. New balance: Rs: {self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs: {amount:.2f}. New balance: Rs: {self.balance:.2f}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.balance

account = BankAccount("Kaushik", 500)
account.deposit(200)
account.withdraw(150)
print(f"Final Balance: Rs: {account.get_balance():.2f}")
