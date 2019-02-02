class Aquatic:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"


class Ambulatory:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"


class Penquin(Ambulatory, Aquatic):
    def __init__(self, name):
        Ambulatory.__init__(self, name=name)
        Aquatic.__init__(self, name=name)

jaws = Aquatic("Jaws")
lassie = Ambulatory("Lasie")
captain_cook = Penquin("Captain Cook")

print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())

print(f"captain_cook is instance of Penquin: {isinstance(captain_cook, Penquin)}")
print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")
