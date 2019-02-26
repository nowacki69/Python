# Write a function called last_element. This function takes in one parameter (a list) and returns
# the last value in the list. It should return None if the list is empty.
def last_element(aList):
    if len(aList) > 0: return aList[-1]
    return None

print(last_element([1,2,3])) # 3
print(last_element([])) # None
