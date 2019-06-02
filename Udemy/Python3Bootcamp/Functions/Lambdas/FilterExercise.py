def remove_nagatives(list_numbers):
    return list(filter(lambda num: num >= 0, list_numbers))

nums = [-1, 3,4, -99]
print(remove_nagatives(nums))
