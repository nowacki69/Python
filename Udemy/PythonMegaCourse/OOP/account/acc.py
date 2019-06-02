class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())


    def withdrawal(self, amount):
        self.balance -= amount


    def deposit(self, amount):
        self.balance += amount

        
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee


    def transfer(self, amount):
        self.balance -= (amount + self.fee)
        

checking = Checking("balance.txt", 1)
checking.deposit(10)
checking.transfer(500)
print(checking.balance)
checking.commit()


# account = Account("balance.txt")
# print(account.balance)
# account.withdrawal(100)
# account.deposit(200)
# print(account.balance)
# account.commit()

