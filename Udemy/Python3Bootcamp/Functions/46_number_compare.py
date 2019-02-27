# Write a function called number_compare. This function takes in two parameters (both numbers). If
# the first is greater than the second, this function returns "First is greater". If the second
# number is greater than the first, this function returns "Second is greater". Otherwise the
# function returns "Numbers are equal"
def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"

    return "Numbers are equal"

print(number_compare(1,1)) # "Numbers are equal"
print(number_compare(1,0)) # "First is greater"
print(number_compare(2,4)) # "Second is greater"
