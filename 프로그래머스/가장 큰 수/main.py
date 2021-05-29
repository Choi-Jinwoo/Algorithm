from functools import cmp_to_key
from itertools import permutations


def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length / len(string_to_expand)) + 1))[:length]


def compare(a, b):
    fixed_a = a
    fixed_b = b

    if len(a) > len(b):
        fixed_b = repeat_to_length(b, len(a))
    elif len(b) > len(a):
        fixed_a = repeat_to_length(a, len(b))

    print(a, b)

    if fixed_b == fixed_a:
        return len(a) - len(b)

    return int(fixed_a) - int(fixed_b)


def solution(numbers):
    numbers = sorted(map(str, numbers), reverse=True, key=cmp_to_key(compare))

    if int(numbers) == 0:
        return '0'

    return ''.join(numbers)


print(solution([0, 0, 0, 0, 0]))
