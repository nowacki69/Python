def add(a, b):
    """
    >>> add(2, 3)
    5
    >>> add(100, 200)
    300
    """
    return a + b


def double(values):
    """ double the value in a list

    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([None])
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

    >>> double([variable])
    Traceback (most recent call last):
    ...
    NameError: name 'variable' is not defined
    """
    return [x * 2 for x in values]


def say_hi():
    """
    >>> say_hi()
    "hi"
    """
    return "hi"


def true_that():
    """
    >>> true_that()
    True
    """
    return True


def make_dict(keys):
    """
    >>> make_dict(['a','b'])
    {'a': True, 'b': True}
    """
    return {key: True for key in keys}


print(add(10, 20))
print(double([1,2,3,4,5,6,7,8,9]))
print(make_dict(['a','b']))
