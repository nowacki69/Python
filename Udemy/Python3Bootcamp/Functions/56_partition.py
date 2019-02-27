# Write a function called partition. This function accepts a list and a callback function (which
# you can assume returns True or False).
# The function should iterate over each element in the list and invoe the callback fucntion at
# each iteration.
#   - If the result of the callback function is True, the element should go into the first list.
#   - If the result of the callback function is False, the element should go into the second list.

# When it's finished, partition should return both lists inside of one larger list.

def partition(aList, fn):
    tList = []; fList = []
    for item in aList:
        if fn(item): tList.append(item)
        if not fn(item): fList.append(item)
    return [tList, fList]

def partition2(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]
def isEven(num):
    return num % 2 == 0


print(partition([1,2,3,4], isEven)) # [[2,4],[1,3]]
print(partition2([1,2,3,4], isEven)) # [[2,4],[1,3]]
