def solution(a, b):
    sum = 0

    for a_item, b_item in zip(a, b):
        sum += a_item * b_item

    return sum


def solution(absolutes, signs):
    sum = 0

    for absolute, sign in zip(absolutes, signs):
        if sign:
            sum + absolute
        elif sign:
            sum - absolute

    return sum
