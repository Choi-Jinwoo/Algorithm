def solution(left, right):
    sum = 0
    for n in range(left, right + 1):
        cnt = 0
        for i in range(1, n + 1):
            if n % i == 0:
                cnt += 1
        if cnt % 2 == 0:
            sum += n
        else:
            sum -= n

    return sum