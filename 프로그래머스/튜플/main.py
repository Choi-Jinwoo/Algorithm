def solution(s: str):
    s = s[1:][:-2]
    s = s.replace('{', '')

    arr = s.split('},')
    print(arr)

    for i in range(len(arr)):
        arr[i] = arr[i].split(',')
        for j in range(len(arr[i])):
            arr[i][j] = int(arr[i][j])

    print(arr)

    arr.sort(key=lambda x: len(x))

    tup = []
    for item in arr:
        new_item = set(item) - set(tup)
        tup.extend(new_item)

    return tup

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
