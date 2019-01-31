nestedList = [[1,2,3], [4,5,6], [7,8,9]]

print(nestedList[0][1])
print(nestedList[-1][1])
print()

# Iteration through a nested loop
for x in nestedList:
    for val in x:
        print(val)

print()

board = [["*" for x in range(1,4)] for y in range(1, 4)]
print(board)
print()


# Another example...
coords = [[10.243, 9.132], [37.212, -14.092], [21.367, 32.572]]
for loc in coords:
    print("Location: " + str(loc))
    for coord in loc:
        print(coord)
    print()
    
print()

# Create a list of lists with this value [[0,1,2],[0,1,2],[0,1,2]] using a
# nested list comprehension and ranges.
answer = [[num for num in range(3)] for x in range(3)]
print(answer)
print()

# Same as above but 0 - 9.
answer = [[num for num in range(10)] for x in range(10)]
print(answer)
print()
