# Custom For Loop

# Normal For Loop examples
# for num in [1,2,3]:
#     print(num)
#
# for char in "hi there":
#     print(char)


# My new For Loop
def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)


def square(x):
    print(x ** 2)


my_for("hello", print)
print()

my_for([1,2,3,4], square)
