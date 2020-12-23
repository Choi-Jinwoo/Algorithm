def get_left_right_top_bottm(n, x, y, power):
    left_x = x - power if x - power >= 0 else 0
    right_x = x + power if x + power < n else n - 1
    top_y = y - power if y - power >= 0 else 0
    bottom_y = y + power if y + power < n else n - 1

    return [left_x, right_x, top_y, bottom_y]


test_case_cnt = int(input())
result = []

for i in range(test_case_cnt):
    n, bomb_cnt = input().split()
    n = int(n)
    bomb_cnt = int(bomb_cnt)

    board = []

    for i in range(n):
        nums = input().split()
        int_nums = [int(num) for num in nums]

        board.append(int_nums)

    kill_point_scope = []

    for i in range(bomb_cnt):
        y, x, power = input().split()
        x = int(x)
        y = int(y)
        power = int(power)

        left_x, right_x, top_y, bottom_y = get_left_right_top_bottm(n, x, y, power)

        for curr_x in range(left_x, right_x + 1):
            kill_point_scope.append((curr_x, y))

        for curr_y in range(top_y, bottom_y + 1):
            kill_point_scope.append((x, curr_y))

    kill_cnt = 0

    set_kill_points = set(kill_point_scope)
    for p in set_kill_points:
        kill_cnt += board[p[1]][p[0]]

    result.append(f'#{i + 1} {kill_cnt}')

for r in result:
    print(r)

