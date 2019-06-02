# Define a function contains_purple that accepts any number of argurments. It
# should return True if any of the arguments are "purple" (all lowercase).
# Otherwise, it should return False.

def contains_purple(*args):
    if "purple" in args: return True
    return False

print(contains_purple(25, 'purple'))

print(contains_purple('green', False, 37, 'blue', "hello world"))

print(contains_purple('purple'))

print(contains_purple('a', 99, 'blah blah blah', 1, True, False, 'purple'))

print(contains_purple(1,2,3))
