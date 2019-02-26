# Write a function called once. This function accepts a function and retruns a new function that can only be invoked
# once. IF the function is invoked more that once, it should return None. Hint you will need to define a new function
# inside of your once function and return that function. You can add properties to your inner function to see if it
# has run already.
def once(fn):
    count = 0
    def inner(a, b):
        nonlocal count
        if count > 0: return None
        count += 1
        return fn(a, b)
    return inner


def add(a,b):
    return a+b


oneAddition = once(add)

print(oneAddition(2,2)) # 4
print(oneAddition(2,2)) # None
print(oneAddition(12,200)) # None
