# Write a function interleave that accepts two strings. It should return a new string containging
# the 2 strings interwoven or zipped together.

def interleave(string1, string2):
    return ''.join(''.join(x) for x in (zip(string1, string2)))

#   OR

def interleave2(string1, string2):
    new_string = ''
    result = list(zip(string1, string2))
    for x, y in result:
        new_string += x + y
    return new_string

s1 = 'Walter'
s2 = 'wizard'
print(interleave(s1, s2))

print(interleave('hi', 'ha'))
print(interleave2('aaa', 'zzz'))
print(interleave2('lzr', 'iad'))
