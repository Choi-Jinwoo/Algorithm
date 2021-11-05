import itertools


def solution(numbers):
    combs = list(itertools.combinations(numbers, 2))

    result = sorted([sum(comb) for comb in combs])

    return result
