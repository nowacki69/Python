class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species = "Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")

blue = Cat("Blue", 'Scottish Fold', 'String')

# Because of inheritance, a Cat has access to:
blue.make_sound("Meow")
print(blue.species)
print(blue.toy)

#blue is both a Cat and Animal (and base object)
print(isinstance(blue, Cat))
print(isinstance(blue, Animal))
print(isinstance(blue, object))
