def rotate(board, query):
    y1, x1, y2, x2 = query

    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    x, y = x1, y1

    temp = board[y][x]
    board[y][x] = board[y + 1][x]
    rotated_values = [temp]
    x += 1

    while x <= x2:
        curr_value = board[y][x]
        board[y][x] = temp
        temp = curr_value
        rotated_values.append(temp)
        x += 1
    x -= 1
    y += 1

    while y <= y2:
        curr_value = board[y][x]
        board[y][x] = temp
        temp = curr_value
        rotated_values.append(temp)
        y += 1
    y -= 1
    x -= 1

    while x >= x1:
        curr_value = board[y][x]
        board[y][x] = temp
        temp = curr_value
        rotated_values.append(temp)
        x -= 1
    x += 1
    y -= 1

    while y > y1:
        curr_value = board[y][x]
        board[y][x] = temp
        temp = curr_value
        rotated_values.append(temp)
        y -= 1

    return board, min(rotated_values)


def solution(rows, columns, queries):
    board = []

    for r in range(0, rows):
        board.append(list(range(r * columns + 1, (r + 1) * columns + 1)))

    min_values = []
    for query in queries:
        board, min_value = rotate(board, query)
        min_values.append(min_value)

    return min_values

