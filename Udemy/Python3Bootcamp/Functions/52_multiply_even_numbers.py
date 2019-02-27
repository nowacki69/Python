# Write a function called multiply_even_numbers. This function accepts a list of numbers and
# returns the product of all even numbers in the list.
def multiply_even_numbers(aList):
    product = 1
    for x in aList:
        if x%2 == 0:
            product *= x
    return product


print(multiply_even_numbers([2,3,4,5,6]))   # 48
