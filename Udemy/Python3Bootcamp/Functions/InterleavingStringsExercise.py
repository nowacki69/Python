def interleave(string1, string2):
    return ''.join(''.join(x) for x in (zip(string1, string2)))

#   OR

    new_string = ''
    result = list(zip(string1, string2))
    for x, y in result:
        new_string += x + y
    return new_string

s1 = 'Walter'
s2 = 'wizard'
print(interleave(s1, s2))
