def solution(dirs):
    x, y = 0, 0

    length = 0
    paths = []
    for dir in dirs:
        pre_x, pre_y = x, y
        if dir == 'U':
            if y >= 5:
                continue
            y += 1
        elif dir == 'D':
            if y <= -5:
                continue
            y -= 1
        elif dir == 'L':
            if x <= -5:
                continue
            x -= 1
        elif dir == 'R':
            if x >= 5:
                continue
            x += 1

        for path in paths:
            path_point_1 = [path[0], path[1]]
            path_point_2 = [path[2], path[3]]
            if [pre_x, pre_y] == path_point_1 and [x, y] == path_point_2 \
                    or [x, y] == path_point_1 and [pre_x, pre_y] == path_point_2:
                break
        else:
            length += 1
            paths.append((pre_x, pre_y, x, y))

    return length


print(solution('LULLLLLLU'))
