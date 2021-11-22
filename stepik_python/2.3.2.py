import itertools
import math


def primes():
    def is_prime(val):
        return (math.factorial(val - 1) + 1) % val == 0

    value = 1
    while True:
        value += 1
        if is_prime(value):
            yield value


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
