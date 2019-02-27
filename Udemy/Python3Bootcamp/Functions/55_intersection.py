# Write a function called intersection. This function should accept two lists and return a list
# with the values that are in both input lists.

# flesh out intersection pleaseeeee
def intersection(aList, bList):
    cList = []
    for item in aList:
        if item in bList:
            cList.append(item)
    return cList

def intersect(aList, bList):
    return [item for item in aList if item in bList]

print(intersection([1,2,3], [2,3,4]))                   # [2,3]
print(intersection(['a', 'b', 'z'], ['x', 'y', 'z']))   # ['z']
print()
print(intersect([1,2,3], [2,3,4]))                   # [2,3]
print(intersect(['a', 'b', 'z'], ['x', 'y', 'z']))   # ['z']
