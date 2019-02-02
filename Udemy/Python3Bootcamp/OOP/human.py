class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # def get_age(self):
    #     return self._age
    #
    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    @property
    def age(self):
        return self._age

jane = Human("Jane", "Goodall", -9)
jan = Human("Jane", "Goodall", 13)
print(jane.age)
print(jan.age)
