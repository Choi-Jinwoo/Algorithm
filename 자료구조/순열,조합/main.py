def perm(result, arr, depth, n, k):
    if depth == k:
        result.append(arr.copy())
        return

    for i in range(depth, n):
        arr[i], arr[depth] = arr[depth], arr[i]
        perm(result, arr, depth + 1, n, k)
        arr[i], arr[depth] = arr[depth], arr[i]

    return result


nums = perm([], [1, 2, 3, 4], 0, 4, 2)

print(nums)
