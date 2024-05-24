class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * (self.interest_rate / 100)
        print(f"Applied interest. Current balance: ${self.balance}")

    def __str__(self):
        return f"Balance: ${self.balance}, Interest rate: {self.interest_rate}%"

# Create an instance of BankAccount
account = BankAccount("123456789", "Zainab Samer")

# Perform a deposit of $1000
account.deposit(1000)

# Perform a withdrawal of $500
account.withdraw(500)

# Print the final balance
print(f"Final balance: ${account.get_balance()}")

# Create an instance of SavingsAccount
savings_account = SavingsAccount("987654321", "Zainab Samer", 5)

# Perform a deposit of $1000
savings_account.deposit(1000)

# Apply interest
savings_account.apply_interest()

# Print the balance and interest rate
print(savings_account)
