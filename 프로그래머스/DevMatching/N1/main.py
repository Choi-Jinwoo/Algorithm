def correct_cnt_to_ranking(n):
    if n <= 1:
        return 6

    return 7 - n


def solution(lottos, win_nums):
    cnt = 0
    for win_num in win_nums:
        if win_num in lottos:
            cnt += 1

    zero_cnt = lottos.count(0)

    min_ranking = correct_cnt_to_ranking(cnt)
    max_ranking = correct_cnt_to_ranking(cnt + zero_cnt)

    return [max_ranking, min_ranking]


print(solution([1, 7, 0, 0, 0, 0], [1, 2, 3, 4, 6, 5]))
