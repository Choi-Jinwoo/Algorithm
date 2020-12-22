import math


def solution(progresses, speeds):
    time = []
    for i in range(len(progresses)):
        time.append(math.ceil((100 - progresses[i]) / speeds[i]))

    result = []
    release_cnt = 0
    current_time = time[0]
    for i in range(len(time)):
        if i == len(time) - 1:
            release_cnt += 1
            result.append(release_cnt)
            break

        if current_time < time[i + 1]:
            release_cnt += 1
            result.append(release_cnt)
            release_cnt = 0
            current_time = time[i + 1]
        else:
            release_cnt += 1
    return result


print(solution([93, 30, 55], [1, 30, 5]))
