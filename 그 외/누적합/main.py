arr = [4, 5, 1, 2, 3, 7, 3, 1, 8]

min = arr[0] + arr[1] + arr[2]

for i in range(len(arr) - 2):
    sum = arr[i] + arr[i + 1] + arr[i + 2]

    if sum < min:
        min = sum

print(min)
