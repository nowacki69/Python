class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

user1 = User('Joe', 'Schmo', 35)
user2 = User('Blanca','Cracko', 41)

print(user1.first, user1.last)
print(user2.first, user2.last)
