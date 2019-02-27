# Write a function called compact. This function accepts a list and returns a list of values that
# are truthy values, without any of the falsey valuues.

# def compact(aList):
#     bList = []
#     for item in aList:
#         if item: bList.append(item)
#     return bList

def compact(aList):
    return [item for item in aList if item]


print(compact([0,1,2,"",[], False, {}, None, "All done"])) # [1,2, "All done"]
