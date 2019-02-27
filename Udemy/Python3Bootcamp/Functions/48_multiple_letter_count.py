# Write a function called multiple_letter_count. This function takes in one parameter (a string)
# and returns a dictionary with the keys being the letters and the values being the count of the
# letter.  Hint: use a dictionary comprehension and count().

# flesh out multiple_letter count:
def multiple_letter_count(word):
    letters = {char:word.count(char) for char in word}
    return letters


print(multiple_letter_count("awesome"))        # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
