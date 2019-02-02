class Animal:
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class Fish(Animal):
    pass


d = Dog()
print(d.speak())

f = Fish()
print(f.speak())
