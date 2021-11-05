def get_weight(bride_trucks):
    sum = 0

    for truck in bride_trucks:
        sum += truck[0]

    return sum


def solution(bridge_length, weight, truck_weights):
    sec = 0
    bride_trucks = []

    while True:
        sec += 1
        cur_weight = get_weight(bride_trucks)

        if len(truck_weights) > 0:
            if cur_weight + truck_weights[0] <= weight:
                bride_trucks.append([truck_weights.pop(0), 0])

        for truck in bride_trucks:
            truck[1] += 1

        if len(bride_trucks) == 0 and len(truck_weights) == 0:
            break

        for truck in bride_trucks:
            if truck[1] == bridge_length:
                bride_trucks.remove(truck)
                break
    return sec

