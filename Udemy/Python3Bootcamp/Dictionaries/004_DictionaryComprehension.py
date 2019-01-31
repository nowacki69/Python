# Dictionary comprehension
# {____ : ____ for ____ in ____}

numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key, value in numbers.items()}

print(squared_numbers)
