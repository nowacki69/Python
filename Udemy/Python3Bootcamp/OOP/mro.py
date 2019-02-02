# Method Resolution Order

class A:
    def do_something(self):
        print("Method Defined in: A")


class B:
    def do_something(self):
        print("Method Defined in: B")


class C:
    def do_something(self):
        print("Method Defined in: C")


class D:
    def do_something(self):
        print("Method Defined in: D")


thing = D()
thing.do_something()

print(D.__mro__)
print(D.mro())
help(D)
