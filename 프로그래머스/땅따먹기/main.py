def fn(curr_col, curr_row, land, dp):
    if curr_row >= len(land) - 1:
        return land[curr_row][curr_col]

    cols = [0, 1, 2, 3]
    cols.remove(curr_col)

    max_cnt = 0
    for col in cols:
        cnt = 0
        if dp[curr_row + 1][col] != 0:
            cnt = dp[curr_row + 1][col]
        else:
            cnt = fn(col, curr_row + 1, land, dp)
            dp[curr_row + 1][col] = cnt

        if max_cnt < cnt:
            max_cnt = cnt

    return max_cnt + land[curr_row][curr_col]


def solution(land):
    dp = []
    for i in land:
        dp.append([0, 0, 0, 0])

    return max(fn(0, 0, land, dp), fn(1, 0, land, dp), fn(2, 0, land, dp), fn(3, 0, land, dp))


print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))
