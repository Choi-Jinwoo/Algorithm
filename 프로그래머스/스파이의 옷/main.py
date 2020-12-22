def factorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= 1

    return r


def sol(clothes):
    clothes_dict = {}

    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]] += 1
        else:
            clothes_dict[cloth[1]] = 1

    result = 1
    val_count = 0

    clothes_dict_values = clothes_dict.values()
    for n in clothes_dict_values:
        result *= n

    return result * factorial(len(clothes_dict.keys())) * len(clothes_dict.keys())


print(sol([["1", "A"], ["2", "A"], ["3", "A"], ["4", "B"], ["4", "B"]]))


