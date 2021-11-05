temp = "012"


def convert(num):
    div, mod = divmod(num, 3)

    if div == 0:
        return temp[mod]
    else:
        return convert(div) + temp[mod]


def solution(n):
    return int(''.join(reversed(convert(n))), 3)


print(solution(45))
