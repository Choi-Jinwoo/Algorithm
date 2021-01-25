# TODO: 힙을이용해 다시 풀기
def solution(scoville, k):
    answer = 0

    while not is_all_food_pass(scoville, k):
        if len(scoville) == 0:
            return -1

        if len(scoville) == 1:
            if scoville[0] >= k:
                return answer

            return -1

        min_1 = min(scoville)
        scoville.remove(min_1)
        min_2 = min(scoville)
        scoville.remove(min_2)

        scoville.insert(0, min_1 + min_2 * 2)
        answer += 1


    return answer


def is_all_food_pass(scoville, k):
    for s in scoville:
        if s < k:
            return False

    return True


print(solution([1, 2, 3, 9, 10, 12], 7))
