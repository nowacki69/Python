# Write a function called decrement_list that accepts a single list of numbers as a parameter. It
# should return a copy of the list where each item has been decremented by one. Use map to do this!

def decrement_list(list_numbers):
    new_nums = list(map(lambda num: num - 1, list_numbers))
    return new_nums

# OR

    for i in range(len(list_numbers)):
        list_numbers[i] = list_numbers[i] - 1
    return list_numbers

nums = [1,2,3,4,5]
print(decrement_list(nums))
print(decrement_list([1,2,3]))
print(decrement_list([20, 14, 11]))
