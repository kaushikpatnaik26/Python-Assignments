class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs: {amount:.2f}. New balance: Rs: {self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew Rs: {amount:.2f}. New balance: Rs: {self.__balance:.2f}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

account = BankAccount("Kaushik", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Final Balance: Rs: {account.get_balance():.2f}")
