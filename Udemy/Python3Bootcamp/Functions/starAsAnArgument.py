def sumAllValues(*args):
    total = 0
    for num in args:
        total += num
    print(total)


nums = [1, 2, 3, 4, 5, 6]

# The * tells Python to unpack each value in a list or tuple and pass each one
# through individually.
sumAllValues(*nums)
