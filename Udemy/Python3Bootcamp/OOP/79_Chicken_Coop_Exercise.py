# Suppose we have a bit ol chicken coop in our backyard full of very productive hens. We're going to model our chickens
# with python! We want to keep track of how many eggs each individual Chicken lays, and at the same time we want to
# track the total number of eggs all hens have laid.

# Create a Chicken class. Each Chicken has a species and a name, as well as an integer attribute called eggs. eggs
# should always start at 0.

# Each Chicken should also have an instance method called lay_egg() which should increment and then return that
# particular Chicken's eggs attribute. lay_eff() should also increment a class variable called total_eggs.


class Chicken:
    total_eggs = 0

    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1


c1 = Chicken(name='Alice', species='Partridge Silkie')
c2 = Chicken(name='Amelia', species='Speckled Sussex')

print(Chicken.total_eggs)
c1.lay_egg()
print(Chicken.total_eggs)
c2.lay_egg()
c2.lay_egg()
print(Chicken.total_eggs)
