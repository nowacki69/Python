# Write a funcion called list_check, which accepts a list and returns True if each value in the list is a list.
# Otherwise the function should return Falseself.
def list_check(aList):
    for item in aList:
        if not isinstance(item, list): return False
    return True



print(list_check([[],[1],[2,3], (1,2)])) # False
print(list_check([1, True, [],[1],[2,3]])) # False
print(list_check([[],[1],[2,3]])) # True
