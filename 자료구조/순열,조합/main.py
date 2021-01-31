from itertools import permutations
from itertools import combinations


def perm(result, arr, depth, n, k):
    if depth == k:
        result.append(arr.copy()[:k])
        return

    for i in range(depth, n):
        arr[i], arr[depth] = arr[depth], arr[i]
        perm(result, arr, depth + 1, n, k)
        arr[i], arr[depth] = arr[depth], arr[i]

    return result


print(perm([], [1, 2, 3, 4], 0, 4, 2))

p = []
c = []
items = [1, 2, 3, 4]

print(list(permutations(items, 2)))
print(list(combinations(items, 2)))
