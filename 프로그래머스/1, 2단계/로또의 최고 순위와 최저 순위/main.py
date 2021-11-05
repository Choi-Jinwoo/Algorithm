def calc_rank(n):
    if n < 2:
        return 6
    return 7 - n


def solution(lottos, win_nums):
    sum = 0
    zero_count = 0

    for lotto in lottos:
        if lotto == 0:
            zero_count += 1
            continue

        if lotto in win_nums:
            sum += 1

    max_sum = sum + zero_count
    min_sum = sum

    return [calc_rank(max_sum), calc_rank(min_sum)]
