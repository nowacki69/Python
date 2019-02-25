# Write a function called sum_pairs which accepts a list and a number and returns the first pair of numbers that sum
# to the number passed to the function.

def sum_pairs(pairs, total):
    for i in range(0, len(pairs) -1):
        if pairs[i] + pairs[i + 1] == total:
            return [pairs[i], pairs[i + 1]]
    return []


print(sum_pairs([4,2,10,5,1], 6)) # [4,2]
print(sum_pairs([11,20,4,2,1,5], 100)) # []
