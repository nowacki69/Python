# Write a function called vowel_count that accepts a string and returns a dictionary with the keys as the vowels and
# values as the count of times that vowel appears in the string.

def vowel_count(string):
    counts = dict()
    for char in string:
        if char.lower() in 'aeiou':
            if not char.lower() in counts: counts[char.lower()] = 0
            counts[char.lower()] += 1
    return counts

print(vowel_count('awesome'))   # {'a': 1, 'e': 2, 'o': 1}
print(vowel_count('Elie'))      # {'e': 2, 'i': 1}
print(vowel_count('Colt'))      # {'o': 1}
