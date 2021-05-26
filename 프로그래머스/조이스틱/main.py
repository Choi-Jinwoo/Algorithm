# BFS

def diff_char(c):
    diff_a = abs(ord(c) - ord('A'))
    diff_z = abs(ord(c) - ord('Z')) + 1

    return min(diff_a, diff_z)


def solution(name):
    queue = [['A' * len(name), 0, 0]]
    last_index = len(name) - 1

    while len(queue) > 0:
        current_name, index, cnt = queue.pop(0)
        if current_name == name:
            return cnt - 1

        cnt += diff_char(name[index]) + 1
        current_name = current_name[:index] + name[index] + current_name[index + 1:]

        if index - 1 < 0:
            queue.append([current_name, last_index, cnt])
        else:
            queue.append([current_name, index - 1, cnt])

        if index + 1 > last_index:
            queue.append([current_name, 0, cnt])
        else:
            queue.append([current_name, index + 1, cnt])


print(solution('JAN'))
