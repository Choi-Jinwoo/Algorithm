def solution(n, a, b):
    answer = 0

    a -= 1
    b -= 1

    while True:
        answer += 1

        if a // 2 == b // 2:
            return answer

        a = a // 2
        b = b // 2

    return answer


print(solution(8, 1, 6))
