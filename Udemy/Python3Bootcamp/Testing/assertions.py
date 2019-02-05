def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive"
    return x + y


print(add_positive_numbers(1, 1))
print(add_positive_numbers(1, -1))
