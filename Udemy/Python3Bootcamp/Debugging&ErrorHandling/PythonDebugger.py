def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        return ("You cannot divide by zero!")
    except TypeError:
        return ("a and b must be ints or floats")
    else:
        return (f"{a} divided by {b} is {result}")


print(divide(1, 2))

import pdb; pdb.set_trace()

print(divide(2, 0))
print(divide('a', 3))
