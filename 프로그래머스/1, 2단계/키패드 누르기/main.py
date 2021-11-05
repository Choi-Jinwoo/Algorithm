keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ['*', 0, '#']
]


def get_n_x_y(n):
    for i in range(len(keypad)):
        for j in range(len(keypad[i])):
            if n == keypad[i][j]:
                return j, i


def solution(numbers, hand):
    lx, ly = 0, 3
    rx, ry = 2, 3

    result = []
    for n in numbers:
        nx, ny = get_n_x_y(n)

        if nx == 0:
            result.append('L')
            lx = nx
            ly = ny
            continue
        elif nx == 2:
            result.append('R')
            rx = nx
            ry = ny
            continue

        l_diff = abs(lx - nx) + abs(ly - ny)
        r_diff = abs(rx - nx) + abs(ry - ny)

        print(n, lx, ly, rx, ry, l_diff, r_diff)

        if l_diff < r_diff:
            result.append('L')
            lx = nx
            ly = ny
        elif r_diff < l_diff:
            result.append('R')
            rx = nx
            ry = ny
        elif hand == 'left':
            result.append('L')
            lx = nx
            ly = ny
        elif hand == 'right':
            result.append('R')
            rx = nx
            ry = ny
    return ''.join(result)


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
