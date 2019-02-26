# The pre-written count_dollar_signs function is broken. It's supposed to return the number of $
# characters in a given string. For some reason, the function always returns either 0 or 1
# What's going on?

# Without adding any new lines of code, make count_dollar_signs work as intended
def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
#       return count
    return count        # This line was indented too far to the right!

print(count_dollar_signs("$uper $ize"))
