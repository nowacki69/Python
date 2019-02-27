# Write a function that accepts a single list full of numbers. t should return the magnitude of the
# number with the largest magnitude (the number that is furthest away from zero).

# Hint: Use max and abs!

def max_magnitude(nums):
    max = 0
    for num in nums:
        if abs(num) > max: max = abs(num)
    return max


def max_magnitude2(nums):
    return max(abs(num) for num in nums)


print(max_magnitude([300, 20, -900]))
print(max_magnitude([10,11,12]))
print(max_magnitude([-5,-1,-89]))

print(max_magnitude2([-10, 5, 0, -3]))
