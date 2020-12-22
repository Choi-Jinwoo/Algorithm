arr = [1,2,4,2,4,5]


def selection_sort(arr):
    for j in range(len(arr) - 1):
        minV = arr[j]
        minP = j

        for i in range(j + 1, len(arr)):
            if minV > arr[i]:
                minV = arr[i]
                minP = i

        arr[j], arr[minP] = minV, arr[j]


selection_sort(arr)
print(arr)
