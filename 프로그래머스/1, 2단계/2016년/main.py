def solution(a, b):
    set_1 = [1, 3, 5, 7, 8, 10, 12]
    set_2 = [4, 6, 9, 11]

    cnt = 0
    for m in range(1, a):
        if m in set_1:
            cnt += 31
        elif m in set_2:
            cnt += 30
        else:
            cnt += 29

    cnt += b - 1
    print(cnt)

    date = cnt % 7
    print(date)
    diff_date = 5 + date
    diff_date %= 7

    if diff_date == 0:
        return 'SUN'
    elif diff_date == 1:
        return 'MON'
    elif diff_date == 2:
        return 'TUE'
    elif diff_date == 3:
        return 'WED'
    elif diff_date == 4:
        return 'THU'
    elif diff_date == 5:
        return 'FRI'
    elif diff_date == 6:
        return 'SAT'


print(solution(3, 1))
