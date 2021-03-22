def solution(brown, yellow):
    max_len = brown // 2

    for h in range(3, max_len):
        for w in range(3, max_len):
            if (w + h) * 2 - 4 == brown and (w - 2) * (h - 2) == yellow:
                return [w, h]


print(solution(10, 2))
