# Write a function called remove_negatives that accepts a list of numbers and returns a copy of the
# lists with all negative numbers removed. Use filter() in your implementation, not a list
# comprehension


def remove_negatives(list_numbers):
    return list(filter(lambda num: num >= 0, list_numbers))

nums = [-1, 3,4, -99]
print(remove_negatives(nums))
print(remove_negatives([-7,0,1,2,3,4,5]))
print(remove_negatives([50,60,70]))
