def solution(prices):
    times = [0] * len(prices)
    for i in range(len(prices) - 1):
        time = 0
        for j in range(i, len(prices) - 1):
            if prices[i] > prices[j]:
                break
            time += 1
        times[i] = time

    print(times)


solution([1, 2, 3, 2, 3, 3, 1])
