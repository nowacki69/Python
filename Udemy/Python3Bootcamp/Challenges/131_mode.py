# Write a function called mode. This function accepts a list of numbers and returns the most
# frequent number in the list of numbers. You can assume that the mode will be unique.
def mode(aList):
    numbers = dict()
    for value in aList:
        if not value in numbers:
            numbers[value]=1
        else:
            numbers[value] += 1
    mode_val = max(numbers.values())
    return list(numbers.keys())[list(numbers.values()).index(mode_val)]



print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])) # 4
