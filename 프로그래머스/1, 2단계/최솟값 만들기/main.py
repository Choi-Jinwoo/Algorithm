# 시간 초과 코드
# def solution(A, B):
#     min_sum = 0
#     arr_len = len(A)
#
#     for i in range(arr_len):
#         min_value = min(A)
#         max_value = max(B)
#
#         A.remove(min_value)
#         B.remove(max_value)
#
#         min_sum += (min_value * max_value)
#
#     return min_sum

def solution(a: list, b: list):
    a.sort()
    b.sort(reverse=True)

    min_sum = 0
    for i in range(len(a)):
        min_sum += (a[i] * b[i])

    return min_sum
