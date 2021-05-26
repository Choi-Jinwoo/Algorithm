import math


def is_double(d):
    if int(d) == 0:
        if d == 0:
            return False
        return True

    if d % int(d) != 0.0:
        return True
    return False


def get_pass_block_cnt(w, h):
    if w < h:
        w, h = h, w

    angle = -1 * (h / w)
    y_addition = h

    pre_x = None
    cnt = 0
    for y in range(h + 1):
        x = (y - y_addition) / angle

        if y > 0:
            cnt += (math.ceil(x) - math.floor(pre_x))

        pre_x = x

    return cnt


def solution(w, h):
    gcd = math.gcd(w, h)

    cnt = get_pass_block_cnt(w // gcd, h // gcd)
    return w * h - cnt * gcd
