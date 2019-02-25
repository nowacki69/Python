# Write a function that takes a string of parentheses, and determines if the order of the
# parentheses is valid. valid_parentheses should return true if the string is valid, and
# false if it it's invalid.


def valid_parentheses(string):
    sum = 0
    for char in string:
        if char == ")": sum -= 1
        if char == "(": sum += 1
        if sum < 0: return False
    return sum == 0


print(valid_parentheses("()")) # True
print(valid_parentheses(")(()))")) # False
print(valid_parentheses("(")) # False
print(valid_parentheses("(())((()())())")) # True
print(valid_parentheses('))((')) # False
print(valid_parentheses('())(')) # False
print(valid_parentheses('()()()()())()(')) # False
