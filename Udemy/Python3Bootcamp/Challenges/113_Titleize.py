# Write a function called titleize which accepts a string of words and returns a new string with the first letter of
# every word in the string capitalized.

def titleize(string):
    new_string = string.split(' ')
    capitalized = []
    for word in new_string:
        new_word = word[0].upper() + word[1:]
        capitalized.append(new_word)
    return ' '.join(capitalized)

def titleize2(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))

print(titleize('this is awesome')) # "This Is Awesome"
print(titleize2('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"
