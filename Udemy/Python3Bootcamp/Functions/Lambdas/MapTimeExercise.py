def decrement_list(list_numbers):
    new_nums = list(map(lambda num: num - 1, list_numbers))
    return new_nums

# OR

    for i in range(len(list_numbers)):
        list_numbers[i] = list_numbers[i] - 1
    return list_numbers

nums = [1,2,3,4,5]
print(decrement_list(nums))
