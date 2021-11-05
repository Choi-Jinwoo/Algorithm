# 테스트 케이스 9번 제외 통과
def solution(citations: list):
    citations.sort(reverse=True)

    for i in range(0, len(citations)):
        if citations[i] <= i:
            return i

    return 0


print(solution([10, 11, 12, 13]))
