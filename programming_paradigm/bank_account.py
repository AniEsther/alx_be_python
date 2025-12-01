class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if funds are enough. Return True/False."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance."""
        print(f"Current account balance: ₦{self.account_balance}")