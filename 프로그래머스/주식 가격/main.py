def get_time(prices):
    time = 0

    for i in range(len(prices)):
        if i < len(prices) - 1:
            if prices[i] <= prices[i + 1]:
                time += 1
            elif i != 0 and prices[i] >= prices[i - 1]:
                time += 1

    return time


def solution(prices):
    times = []
    prices_len = len(prices)

    for i in range(prices_len):
        times.append(get_time(prices))
        prices.pop(0)

    return times


print(solution([1,2,3,2,3]))