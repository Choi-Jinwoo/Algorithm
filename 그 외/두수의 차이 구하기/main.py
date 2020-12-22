n = 10


def sum_pow(n):
    n_sum = n * (n + 1) // 2
    return pow(n_sum, 2)


def pow_sum(n):
    n_sum = 0
    for i in range(1, n + 1):
        n_sum += pow(i, 2)
    return n_sum


n_sum_pow = sum_pow(n)
n_pow_sum = pow_sum(n)

a = max(n_sum_pow, n_pow_sum)
b = min(n_sum_pow, n_pow_sum)

print(a - b)
