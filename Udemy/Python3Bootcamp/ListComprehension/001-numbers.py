numbers = [1, 2, 3, 4, 5]
# Double all numbers in numbers list
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)


# All numbers found in both lists
answer = [num for num in [1,2,3,4] if num in [3,4,5,6]]
print(answer)


# All numbers from 1 to 100 (including  100) divisible by 12
answer =  [num for num in range(1, 101) if num % 12 == 0]
print(answer)


# Take a string and return all characters that are not vowels.
answer = [char for char in "amazing" if char not in "aeiou"]
print(answer)
