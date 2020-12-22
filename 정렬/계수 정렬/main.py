arr = [5, 2, 4, 1, 4, 2]
k = 5


def counting_sort(arr):
    # counting 배열 생성, 정렬된 값들이 복사될 배열
    # 1. 대상 배열의 요소들이 몇번씩 나왔는지 확인
    # 2. 카운팅 배열 누적합 구하기 (배열요소가 몇번째 위치해야 하는지 계산)
    # 3. 대상 배열 순회하며 위치 찾아 넣기

    count = [0, 0, 0, 0, 0, 0]  # 0으로 초기화(크기는 k + 1)
    sorted_arr = []

    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(1, k + 1):
        count[i] = count[i - 1] + count[i]

    for i in range(len(arr)):
        sorted_arr[--count[arr[i]]] = arr[i]
