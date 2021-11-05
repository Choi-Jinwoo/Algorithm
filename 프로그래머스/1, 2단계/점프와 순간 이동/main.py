def solution(n):
    k = 0
    while True:
        if n == 1 or n == 2:
            k += 1
            return k
        div, mod = divmod(n, 2)
        if mod == 1:
            k += 1

        n = div


print(solution(5000))
