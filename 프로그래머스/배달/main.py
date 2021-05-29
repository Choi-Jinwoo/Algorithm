def calc_time(towns):
    stack = [[0, 0]]

    visited = {}
    while len(stack):
        town, time = stack.pop()

        if town not in visited:
            visited[town] = time
        elif visited[town] > time:
            visited[town] = time
        else:
            continue

        for i in range(len(towns[town])):
            next_town = towns[town][i]
            stack.append([next_town['next'], time + next_town['distance']])

    return visited


def solution(N, roads, K):
    towns = [[] for _ in range(N)]

    for road in roads:
        towns[road[0] - 1].append({'next': road[1] - 1, 'distance': road[2]})
        towns[road[1] - 1].append({'next': road[0] - 1, 'distance': road[2]})

    cnt = 0
    visited = calc_time(towns)
    for time in visited.values():
        if time <= K:
            cnt += 1

    return cnt


print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
