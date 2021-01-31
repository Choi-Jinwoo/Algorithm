def perm(result: list, arr: list, depth, k):
    if depth == k:
        result.append(''.join(map(str, arr)))
        return

    for i in range(depth, len(arr)):
        arr[i], arr[depth] = arr[depth], arr[i]
        perm(result, arr, depth + 1, k)
        arr[i], arr[depth] = arr[depth], arr[i]


def solution(numbers):
    result = []
    perm(result, numbers, 0, len(numbers))

    int_result = map(int, result)
    return str(max(int_result))


print(solution([0, 0, 0]))
