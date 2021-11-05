import heapq


def solution(scoville, k):
    heap = scoville
    heapq.heapify(heap)

    answer = 0
    while True:
        if len(heap) <= 1:
            if heap[0] >= k:
                break
            answer = -1
            break

        min_val = heapq.heappop(heap)

        if min_val >= k:
            break

        min_val_2 = heapq.heappop(heap)

        heapq.heappush(heap, min_val + min_val_2 * 2)
        answer += 1

    return answer


print(solution([8], 7))
