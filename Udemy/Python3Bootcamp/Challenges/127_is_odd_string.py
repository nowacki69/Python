# Write a function called ois_odd_string which returns true if sum of each character's position in
# the alphbet is odd. For example, 'a' is in the first position, 'b' is in the second position, and
# so on. If the sum is even, return False. NOTE: INDEXING STARTS AT 1. A is position 1, NOT
# POSITION 0.
def is_odd_string(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sum = 0
    for char in string:
        sum += alphabet.index(char) + 1
    if sum % 2 == 0: return False
    return True


print(is_odd_string('a')) # True
print(is_odd_string('aaaa')) # False
print(is_odd_string('amazing')) # True
print(is_odd_string('veryfun')) # True
print(is_odd_string('veryfunny')) # False
