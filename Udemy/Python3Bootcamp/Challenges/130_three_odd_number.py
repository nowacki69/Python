# Write a function called three_odd_numbers, which accepts a list of numbers and returns True if
# any three consecutive numbers sum to an odd numberself.

def three_odd_numbers(aList):
    start = 0
    end = 3
    length = len(aList)
    while end <= length:
        bList = aList[start:end]
        group_sum = (sum(bList))
        if group_sum % 2 == 1: return True
        start += 1
        end += 1
    return False

print(three_odd_numbers([1,2,3,4,5])) # True
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
print(three_odd_numbers([5,2,1])) # False
print(three_odd_numbers([1,2,3,3,2])) # False
