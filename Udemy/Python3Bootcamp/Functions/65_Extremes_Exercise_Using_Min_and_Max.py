# Write a function extremes which accepts an iterable. It should return a tuple containing the
# minimum and maximum elements.


def extremes(theList):
    return (min(theList), max(theList))

print(extremes([1,2,3,4,5]))
print(extremes(['a', 'b', 'c']))
print(extremes('alcatraz'))
