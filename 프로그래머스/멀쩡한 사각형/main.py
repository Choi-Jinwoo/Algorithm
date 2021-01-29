def is_double(d):
    if int(d) == 0:
        if d == 0:
            return False
        return True

    if d % int(d) != 0.0:
        return True
    return False


def solution(w, h):
    angle = -1 * (h / w)
    y_addition = h

    x_arr = []
    cnt = 0
    for y in range(h + 1):
        x_arr.append((y - y_addition) / angle)

    print(x_arr)
    cnt = 0
    for i in range(len(x_arr) - 1):
        cnt += int(x_arr[i]) - int(x_arr[i + 1])

        if i != 0 and is_double(x_arr[i]):
            cnt += 1

    return w * h - cnt


print(solution(8, 12))
