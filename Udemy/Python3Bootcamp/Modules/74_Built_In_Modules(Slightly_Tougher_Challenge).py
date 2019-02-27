# Define a function called contains_keyword that accepts any number of string
# arguments. It should return True if any of the arguments are considered
# Python keywords.  Otherwise it should return False. Python has a built-in
# module called 'keyword' that contains a method called 'iskeyword'. import
# keyword and then use keyword.iskeyword in your own function to determine if a
# given string is a keyword

import keyword


def contains_keyword(*args):
    for arg in args:
        if keyword.iskeyword(arg):
            return True
    return False


# Should return False, True, True
print(contains_keyword('hello', 'goodbye'))
print(contains_keyword('def', 'haha', 'lol', 'chicken', 'alaska'))
print(contains_keyword('four', 'for', 'if'))
