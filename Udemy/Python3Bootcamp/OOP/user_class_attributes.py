# A User class with both instance attributes and instance methods


class User:
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        print(f"{self.first} has logged out.")
        User.active_users -= 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}."

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first}!!!"


print(f"{User.active_users} active users.")

user1 = User('Joe', 'Schmo', 35)
user2 = User('Blanca', 'Cracko', 41)

print(user1.full_name(), user1.initials())
print(user2.full_name(), user2.initials())
print(user1.likes("69"))
print(user2.likes('nothing'))
print(user2.is_senior())
print(user1.age)
print(user1.birthday())

print(f"{User.active_users} active users.")
print(user2.logout())
print(f"{User.active_users} active users.")
