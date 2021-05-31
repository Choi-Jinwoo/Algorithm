def solution(s):
    result = [0, 0]
    next = s

    while True:
        result[0] += 1
        result[1] += next.count('0')

        next = format(len(next.count('1') * '1'), 'b')
        if next == '1':
            return result


print(solution('01110'))
