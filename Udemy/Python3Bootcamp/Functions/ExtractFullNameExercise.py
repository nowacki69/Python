'''
Create a function that will accept a list of dictionaries and return a new
list of strings with the first and last name keys in each dictionary
concatenated.
'''


def extract_full_name(names):
    return list((name['first'] + " " + name['last'] for name in names))

#   OR

    return list(map(lambda val: "{} {}".format(val['first'], val['last']), names))


names = [
        {'first': 'Elie', 'last': 'Schoppik'},
        {'first': 'Colt', 'last': 'Steele'}
]

# Should return ['Elie Schoppik', 'Colt Steele']
print(extract_full_name(names))
