# Write a function called capitalize. This function accepts a string and returns the same string
# with the first letter capitalized. You may want to use slices to help you out.
def capitalize(string):
    return string[0].upper() + string[1::]

print(capitalize("tim")) # "Tim"
print(capitalize("matt")) # "Matt"
