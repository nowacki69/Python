# Implement a functin is_all_strings that accepts a single iterable and returns True if it contains
# ONLY strings. Otherwise it should return False.


def is_all_strings(strings):
    """ Checks to see if all items in a list are strings
    >>> is_all_strings(['a','b'])
    True

    >>> is_all_strings([1, 'z'])
    False

    >>> is_all_strings([False, '3'])
    False

    >>> is_all_strings(['z', None])
    False

    """
    return all(type(string) == type('a') for string in strings)

print(is_all_strings(['a','b','c']))
print(is_all_strings([1, 'j']))
