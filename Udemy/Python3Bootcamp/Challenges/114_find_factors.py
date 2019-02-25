# Write a function called find_factors which accepts a number and returns a list of all of the numbers which are is
# divisible by starting from 1 and going up to the number.


def find_factors(number):
    factors = list()
    for factor in range(1, number + 1):
        if number % factor == 0:
            factors.append(factor)
    return factors


print(find_factors(10))        # [1,2,5,10 ]
print(find_factors(11))        # [1,11]
print(find_factors(111))       # [1,3,37,111 ]
print(find_factors(321421))    # [1,293,1097,321421 ]
print(find_factors(412146))    # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
