from functools import cmp_to_key


def get_first_n(n):
    if n < 10:
        return n

    return int(str(n)[0])


def compare(a, b):
    a_f = get_first_n(a)
    b_f = get_first_n(b)

    if a_f == b_f:
        if a < 10 and b < 10:
            return 0

        if a > 10:
            a = int(str(a)[1:])
        else:
            a = 0

        if b > 10:
            b = int(str(b)[1:])
        else:
            b = 0

        return compare(a, b)

    if a_f < b_f:
        return 1

    if a_f > b_f:
        return -1


def solution(numbers):
    sorted_numbers = sorted(numbers, key=cmp_to_key(compare))
    print(sorted_numbers)
    return ''.join(map(str, sorted_numbers))


print(solution([91, 30, 1000, 9, 101]))
