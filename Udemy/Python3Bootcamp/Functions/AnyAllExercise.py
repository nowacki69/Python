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

print(is_all_strings(['a','b']))
print(is_all_strings([1, 'j']))
