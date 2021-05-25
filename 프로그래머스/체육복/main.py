def solution(n, lost, reserve):
    duplicate = list(set(lost) & set(reserve))

    lost = [n for n in lost if n not in duplicate]
    reserve = [n for n in reserve if n not in duplicate]

    result_last = [*lost]
    for lost_person in lost:
        if lost_person - 1 in reserve:
            result_last.remove(lost_person)
            reserve.remove(lost_person - 1)
        elif lost_person + 1 in reserve:
            result_last.remove(lost_person)
            reserve.remove(lost_person + 1)

    return n - len(result_last)


print(solution(5, [2, 4], [1, 3, 5]))
