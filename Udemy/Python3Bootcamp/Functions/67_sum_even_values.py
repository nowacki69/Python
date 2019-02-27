# Write a function called sum_even_values. This function should accept a variable number of
# arguments and return the sum of all the arguments that are divisible by 2. If there are no
# numbers divisible by 2, the function should return 0. To be clear, it accepts all the numbers
# as individual arguments.

def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)


def sum_even_values2(*args):
    return sum(arg for arg in args if arg % 2 == 0)

print(sum_even_values(1,2,3,4,5,6))
print(sum_even_values2(4,2,1,10))
print(sum_even_values(1))
