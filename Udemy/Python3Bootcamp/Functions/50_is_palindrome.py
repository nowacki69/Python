# Write a function called is_palindrome. A palindrome is a word, phrase, number, or other sequence
# of characters which reads the same backward or forward. This function hsould take in one
# parameter and returns True or False depending on whether it is a palindrome. As a bonus, allow
# your function to ignore whitespace and capitization so that is_palindrome('a man a plan a canal
# Panama') returns True.

def is_palindrome(phrase):
    new_phrase = phrase.replace(' ','')
    reversed = new_phrase[::-1]
    if new_phrase.lower() == reversed.lower(): return True
    return False


print(is_palindrome('testing'))                # False
print(is_palindrome('tacocat'))                # True
print(is_palindrome('hannah'))                 # True
print(is_palindrome('robert'))                 # False
print(is_palindrome('amanaplanacanalpanama'))  # True
