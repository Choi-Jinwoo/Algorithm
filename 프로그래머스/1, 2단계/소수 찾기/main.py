from itertools import permutations


def is_prime_num(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while True:
        if i * i > n:
            break

        if n % i == 0:
            return False

        i += 1

    return True


def solution(numbers: str):
    str_nums_arr = []
    for n in numbers:
        str_nums_arr.append(n)

    nums_perm = []
    for i in range(1, len(str_nums_arr) + 1):
        nums_perm.extend(list(permutations(str_nums_arr, i)))

    int_nums_perm = []
    for item in nums_perm:
        int_nums_perm.append(int(''.join(item)))

    int_nums_perm = list(set(int_nums_perm))

    cnt = 0
    for n in int_nums_perm:
        if is_prime_num(n):
            cnt += 1

    return cnt
