# Write a function called find_greater_numbers which accepts a list and returns the number of times a number is
# followed by a larger number across the entire list.

# Take the example find_greater_numbers([6,1,2,7]) #4, there are 4 times where a number is followed by a greater number.

def find_greater_numbers(aList):
    total = 0
    index = (len(aList)) - 1
    while index > 0:
        counter = 1
        while counter <= index:
            if aList[index] > aList[index - counter]: total += 1
            counter += 1
        index -= 1
    return total

print(find_greater_numbers([1,2,3]))        # 3
print(find_greater_numbers([6,1,2,7]))      # 4
print(find_greater_numbers([5,4,3,2,1]))    # 0
print(find_greater_numbers([]))             # 0
