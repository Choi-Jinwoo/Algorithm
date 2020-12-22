from random import random


def is_line_through_line(a, x, y):
    if x < y / a  and y / a < x + 1:
        return True

    return False


def is_line_through_block(w, h, x, y):
    a = h / w
    if is_line_through_line(a, x, y) or is_line_through_line(a, x, y + 1):
        return True
    return False



def solution(w, h):
    through_block_cnt = 0

    for y in range(h):
        for x in range(w):
            if is_line_through_block(w, h, x, y):
                through_block_cnt += 1

    return w * h - through_block_cnt

print(solution(8, 12))


random.randrange(1, 2, 3)
mean