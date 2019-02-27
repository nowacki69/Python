# Define a new class called BankAccount
# - Each BankAccount should have an owner, specified when a new BankAccount is created like BankAccount("Charlie")
# - Each BankAccount should have a balance attribute that always starts out as 0.0
# - Each instance should have a deposit methos that accepts a number and adds it to the balance. It should return the
#   new balance.
# - instance shoud have a withdraw method that accepts a number and subtracts it from the balance. It should return the
#   new balance.


class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


acct = BankAccount("Darcy")
print(acct.owner)
print(acct.balance)
print(acct.deposit(10))
print(acct.withdraw(3))
print(acct.balance)
