def increase(n):
    if n == '4':
        return '11'

    last_str = n[-1]
    if last_str == '1':
        return n[0:len(n) - 1] + '2'

    if last_str == '2':
        return n[0:len(n) - 1] + '4'

    return increase(n[0:len(n) - 1]) + '1'


def solution(n):
    curr_val = ''

    for i in range(1, n + 1):
        if i == 1:
            curr_val = '1'
        elif i == 2:
            curr_val = '2'
        elif i == 3:
            curr_val = '4'
        else:
            curr_val = increase(curr_val)

    print(curr_val)
    return curr_val


print(solution(5))

# print(increase('4'))