n = 3

for i in range(n):
    for j in range(n):
        # 첫번째와 두번째가 같으면 작업 안함
        if i == j:
            continue

        for k in range(n):
            if k == i or k == j:
                continue
            print(i, j, k)