heap = []


# 최소 힙
def insert(data):
    heap.append(data)
    idx = len(heap)

    while True:
        if idx <= 1:
            break

        parent_idx = idx // 2

        if heap[parent_idx - 1] < heap[idx - 1]:
            break

        heap[idx - 1], heap[parent_idx - 1] = heap[parent_idx - 1], heap[idx - 1]
        idx = parent_idx


def delete():
    last_data = heap.pop()
    heap[0] = last_data

    idx = 1
    while True:
        l_child_idx = idx * 2
        r_child_idx = idx * 2 + 1

        if l_child_idx - 1 > len(heap) - 1:
            break

        if r_child_idx - 1 > len(heap) - 1:
            if heap[l_child_idx - 1] < heap[idx - 1]:
                heap[idx - 1], heap[l_child_idx - 1] = heap[l_child_idx - 1], heap[idx - 1]
            break

        if heap[l_child_idx - 1] < heap[r_child_idx - 1]:
            heap[idx - 1], heap[l_child_idx - 1] = heap[l_child_idx - 1], heap[idx - 1]
            idx = l_child_idx
        else:
            heap[idx - 1], heap[r_child_idx - 1] = heap[r_child_idx - 1], heap[idx - 1]
            idx = r_child_idx


insert(18)
insert(13)
insert(5)
insert(3)

print(heap)
insert(4)

print(heap)
