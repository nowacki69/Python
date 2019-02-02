class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls, data_str):
        first,last,age = data_str.split(",")
        return cls(first, last, int(age))

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


class Moderator(User):
    total_mods = 0
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        Moderator.total_mods += 1

    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active mods"

    def remove_post(self):
        return f"{self.full_name} removed a post from the {self.community}"


user1 = User('Joe', 'Schmo', 35)
user2 = User('Blanca', 'Cracko', 41)
# print(User.display_active_users())
user3 = User('Ho', 'Schmo', 53)
user4 = User('Srilake', 'Cracko', 41)
# print(User.display_active_users())

tom = User.from_string("Tom,Jones,89")

# print(tom.full_name())
# print(tom.birthday())

jasmine = Moderator('Jasmine', "O'Connor", 61, "Piano")
print(User.display_active_users())
print(Moderator.display_active_mods())
