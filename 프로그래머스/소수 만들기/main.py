import itertools
import math


def is_prime(num):
    if num == 2:
        return True

    if num == 0 or num == 1 or (num != 2 and num % 2 == 0):
        return False

    for n in range(3, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False

    return True


def solution(nums):
    combs = list(itertools.combinations(nums, 3))

    print(combs)
    primes = [comb for comb in combs if is_prime(sum(comb))]

    return len(primes)


solution([1, 2, 3, 4])
