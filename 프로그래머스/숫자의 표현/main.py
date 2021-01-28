# def solution(n):
#     answer = 0
#
#     for i in range(1, n):
#
#         arr = []
#         for j in range(1, n + 1):
#             arr.append(j)
#
#             if len(arr) >= i:
#                 if sum(arr) == n:
#                     answer += 1
#                     break
#                 elif sum(arr) > n:
#                     break
#
#                 del arr[0]
#
#     return answer


def solution(n):
    answer = 0

    for i in range(1, n):
        min_sum = 0
        for j in range(i):
            min_sum += j
        if min_sum > n:
            break

        center = n // i

        if center == i - 1:
            continue

        start = center - (i - 1) // 2
        end = center + (i - 1) // 2
        if i % 2 == 0:
            end += 1

        if i == 1 and start == n:
            answer += 1
        elif n == sum(range(start, end + 1)):
            answer += 1

    return answer


print(solution(15))
