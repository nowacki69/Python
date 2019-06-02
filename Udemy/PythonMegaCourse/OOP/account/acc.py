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
    """This class generates checking account objects"""

    type="checking"
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee


    def transfer(self, amount):
        self.balance -= (amount + self.fee)
        

johns_checking = Checking("jack.txt", 1)
johns_checking.transfer(100)
print(johns_checking.balance)
johns_checking.commit()
print(johns_checking.type)

jacks_checking = Checking("john.txt", 1)
jacks_checking.transfer(100)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)
print(jacks_checking.__doc__)

# account = Account("balance.txt")
# print(account.balance)
# account.withdrawal(100)
# account.deposit(200)
# print(account.balance)
# account.commit()

