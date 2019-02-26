# Write a function called next_prime, which returns a generator that will yield an unlimited
# number of primes, starting from the first prime (2).

# Recall that a prime number is any whole number that has exactly two divisors: one and the number
# itself. The first few primes are 2, 3, 5, 7, 11, ...
def next_prime():
    primes = []
    x = 1
    while True:
        x += 1
        prime = True
        for x in primes:
            if x % prime == 0: return False
        primes.append(x)
        yield x

primes = next_prime()
[next(primes) for i in range(25)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
