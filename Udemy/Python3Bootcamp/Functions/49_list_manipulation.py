# Write a function called list_manipulation. This function should take in four parameters (a list,
# command, location and value).
#   - If the command is 'remove' and the location is 'end', the function should remove the last
#       value in the list and return the value removed.
#   - If the command is 'remove' and the location is 'beginning', the function should remove the
#       first value in the list and return the value removed.
#   - If the command is 'add' and the location is 'beginning', the function should add the value
#       (fourth parameter) to the beginning of the list and return the list.
#   - If the command is 'add' and the location is 'end', the function shoud add the value (fourth
#       parameter) to the end of the list and return the list.
def list_manipulation(aList, command, location, value = None):
    if command == 'remove' and location == 'end':
            return aList.pop()
    elif command == 'remove' and location == 'beginning':
            return aList.pop(0)
    elif command == 'add' and location == 'end':
            aList.append(value)
            return aList
    elif command == 'add' and location == 'beginning':
            aList.insert(0, value)
            return aList


print(list_manipulation([1,2,3], "remove", "end")) # 3
print(list_manipulation([1,2,3], "remove", "beginning")) #  1
print(list_manipulation([1,2,3], "add", "beginning", 20)) #  [20,1,2,3]
print(list_manipulation([1,2,3], "add", "end", 30)) #  [1,2,3,30]
