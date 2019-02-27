# Write a function that will accept a variable number of arguments. The function
# should return the sum of all the parameters that are floats.  If none are
# floats, return 0


def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)

print(sum_floats(5, 1.1, 2.2, 0, 'shit'))
print(sum_floats(5, 'help', 2, 0, 'shit'))
