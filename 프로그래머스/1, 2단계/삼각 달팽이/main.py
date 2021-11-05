def get_inc(x_inc, y_inc):
    if y_inc < 0 and x_inc < 0:
        return 0, 1
    elif y_inc > 0 and x_inc == 0:
        return 1, 0
    elif x_inc > 0 and y_inc == 0:
        return -1, -1


def solution(n):
    arr = []
    total_cnt = 0

    for i in range(n):
        arr.append([])
        for j in range(0, i + 1):
            total_cnt += 1
            arr[i].append(0)

    x = 0
    y = 0

    x_inc = 0
    y_inc = 1

    cnt = 1

    while True:
        arr[y][x] = cnt
        cnt += 1

        if cnt == total_cnt + 1:
            break

        if y + y_inc > len(arr) - 1:
            x_inc, y_inc = get_inc(x_inc, y_inc)
        elif x + x_inc > len(arr) - 1:
            x_inc, y_inc = get_inc(x_inc, y_inc)

        if arr[y + y_inc][x + x_inc] != 0:
            x_inc, y_inc = get_inc(x_inc, y_inc)

        y += y_inc
        x += x_inc

    result = []
    for item in arr:
        result.extend(item)

    return result


