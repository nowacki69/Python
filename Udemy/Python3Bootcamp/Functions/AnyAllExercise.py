def is_all_strings(strings):
    return all(type(string) == type('a') for string in strings)

print(is_all_strings(['a','b']))
print(is_all_strings([1, 'j']))
