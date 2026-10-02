# Build a BankAccount class:

# __init__(self, owner, balance=0) — sets up an account with an owner's name and a starting balance (default 0 if not specified).
# deposit(self, amount) — adds amount to self.balance, then prints the new balance.
# withdraw(self, amount) — subtracts amount from self.balance, but only if there's enough balance — otherwise print "Insufficient funds" and don't subtract anything.
# show_balance(self) — prints the current balance.

# Then create two separate BankAccount objects, deposit/withdraw from each independently, and confirm their balances don't interfere with each other.

class Bank_Account:
    def __init__(self, owner, balance=0):
        self.name = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(self.balance)
        else:
            print('Insufficient funds')
    def show_balance(self):
        sh_balance = self.balance
        print(sh_balance)

own1 = Bank_Account("Abiodun", 3000)
own2 = Bank_Account("IBK", 2000)

own1.deposit(7000)
own2.withdraw(1000)

own1.show_balance()
own2.show_balance()