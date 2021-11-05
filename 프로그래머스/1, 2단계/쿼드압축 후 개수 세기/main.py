def split_arr(arr):
    arr_1 = []
    arr_2 = []
    arr_3 = []
    arr_4 = []
    size = len(arr) // 2

    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append(arr[i][j])

        arr_1.append(row)

    for i in range(size, len(arr)):
        row = []
        for j in range(0, size):
            row.append(arr[i][j])

        arr_2.append(row)

    for i in range(0, size):
        row = []
        for j in range(size, len(arr)):
            row.append(arr[i][j])

        arr_3.append(row)

    for i in range(size, len(arr)):
        row = []
        for j in range(size, len(arr)):
            row.append(arr[i][j])

        arr_4.append(row)

    return arr_1, arr_2, arr_3, arr_4


def fun(arr, result):
    common_element = arr[0][0]

    is_all_same = True
    for row in arr:
        for element in row:
            if element != common_element:
                is_all_same = False
                break

        if not is_all_same:
            break

    if is_all_same:
        result.append(common_element)
        return

    arr_1, arr_2, arr_3, arr_4 = split_arr(arr)

    fun(arr_1, result)
    fun(arr_2, result)
    fun(arr_3, result)
    fun(arr_4, result)


def solution(arr):
    result = []
    fun(arr, result)

    return [result.count(0), result.count(1)]


print(solution([[1, 1], [1, 1]]))
