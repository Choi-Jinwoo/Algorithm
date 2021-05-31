def reorder(m, n, board):
    for x in range(n):
        stack = []
        for y in range(m):
            if board[y][x] != 0:
                stack.append(board[y][x])

        for y in range(m - 1, -1, -1):
            if len(stack) == 0:
                board[y][x] = 0
            else:
                board[y][x] = stack.pop()


def solution(m, n, board):
    for y in range(m):
        board[y] = list(board[y])

    cnt = 0
    while True:
        delete_points = []
        for y in range(m - 1):
            for x in range(n - 1):
                c = board[y][x]

                if c == 0:
                    continue

                if c == board[y + 1][x] == board[y][x + 1] == board[y + 1][x + 1]:
                    delete_points.append((y, x))
                    delete_points.append((y, x + 1))
                    delete_points.append((y + 1, x))
                    delete_points.append((y + 1, x + 1))

        delete_points = list(set(delete_points))

        if len(delete_points) == 0:
            break

        cnt += len(delete_points)

        for point in delete_points:
            board[point[0]][point[1]] = 0

        reorder(m, n, board)

    return cnt


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
