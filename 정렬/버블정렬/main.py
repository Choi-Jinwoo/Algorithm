
def bubble_sort(arr):
    for j in range(len(arr) - 1):
        for i in range(len(arr) - 1 - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


arr = [1, 5, 1, 3]
bubble_sort(arr)
print(arr)
