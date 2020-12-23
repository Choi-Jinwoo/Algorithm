def diff_char(c):
    diff_a = abs(ord(c) - ord('A'))
    diff_z = abs(ord(c) - ord('Z')) + 1

    return min(diff_a, diff_z)


def is_a_string(name):
    for s in name:
        if s != 'A':
            return False
    return True


def solution(name):
    right_cnt = 0
    left_cnt = 0

    if is_a_string(name):
        return 0

    for i in range(len(name)):
        if is_a_string(name[i:]):
            break

        diff = diff_char(name[i])

        if i == 0:
            right_cnt += diff
        else:
            right_cnt += 1 + diff

    left_cnt = diff_char(name[0])
    name = name[1:]
    name = name[::-1]

    for i in range(len(name)):
        if is_a_string(name[i:]):
            break

        diff = diff_char(name[i])
        left_cnt += diff + 1

    print(right_cnt, left_cnt)
    return min(right_cnt, left_cnt)


print(solution('BBBAAAB'))
