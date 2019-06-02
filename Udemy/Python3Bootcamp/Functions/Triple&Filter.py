# Write a function that accepts a list of numbers, filters out every number that
# is not divisible by 4, and returns a new list where every remaining number is
# tripled.

def triple_and_filter(list_numbers):
    return [num*3 for num in list_numbers if num % 4 ==0]

def triple_and_filter2(list_numbers):
    return list(filter(lambda num: num % 4 == 0, map(lambda num: num*3, list_numbers)))

print(triple_and_filter([1,2,3,4]))
print(triple_and_filter2([1,2,3,4]))
