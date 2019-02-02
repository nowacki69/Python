# Let's pretend we're building an RPG in Python.
# 1 Define a class Character that has the following properties
# - name -- String
# - hp -- an Integer value representing health (aka hitpoints)
# - level -- an integer value representing experience level

# 2 Define a subclass NPC (which stands for Non-Player Character) that inherits from Character, and has an additional
#   instance method called speak which prints the speech that chatacter would say when a player interacts with them.

class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level


class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return "I heard there were monsters running around last night!"


villager = NPC("Bob", 100, 12)
print(villager.name)                       # Bob
print(villager.hp)                         # 100
print(villager.level)                      #  12
print(villager.speak())                    # "I heard there were monsters running around last night!"
