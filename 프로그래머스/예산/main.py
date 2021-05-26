def solution(d, budget):
    cnt = 0

    d.sort()

    for item in d:
        budget -= item
        if budget < 0:
            return cnt
        else:
            cnt += 1

    return cnt


print(solution([1, 3, 2, 5, 4], 9))
