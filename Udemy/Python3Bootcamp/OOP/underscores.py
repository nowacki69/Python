# _name
# __name
# __name__

class Person():
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi"
        self.__msg = "I like turtles!"

p = Person()

print(p.name)
print(p._secret)
print(p._Person__msg)
