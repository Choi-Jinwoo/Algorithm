def rotate(board, q):
    y1, x1, y2, x2 = q
    y1 -= 1
    x1 -= 1
    y2 -= 1
    x2 -= 1

    x, y = x1, y1

    last_y = len(board) - 1
    last_x = len(board[0]) - 1

    result = []

    x_increase, y_increase = 1, 0
    pre = board[y][x]
    result.append(pre)
    while True:
        if x + x_increase > last_x or x + x_increase < 0 or \
                y + y_increase > last_y or y + y_increase < 0 or \
                x + x_increase > x2 or x + x_increase < x1 or \
                y + y_increase > y2 or y + y_increase < y1:
            if x_increase == 1 and y_increase == 0:
                x_increase = 0
                y_increase = 1
            elif x_increase == 0 and y_increase == 1:
                x_increase = -1
                y_increase = 0
            elif x_increase == -1 and y_increase == 0:
                x_increase = 0
                y_increase = -1
            elif x_increase == 0 and y_increase == -1:
                x_increase = 1
                y_increase = 0

        x += x_increase
        y += y_increase

        result.append(board[y][x])
        board[y][x], pre = pre, board[y][x]

        if x == x1 and y == y1:
            break

    return min(result)


def solution(rows, columns, queries):
    cnt = 1
    board = []
    for row in range(rows):
        board.append([])
        for col in range(columns):
            board[-1].append(cnt)
            cnt += 1

    answer = []
    for q in queries:
        answer.append(rotate(board, q))

    return answer


print(solution(3, 3, [[1, 1, 2, 2]]))
