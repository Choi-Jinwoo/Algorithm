def solution(clothes):
    cloth_group_by = {}

    for cloth in clothes:
        if cloth[1] in cloth_group_by:
            cloth_group_by[cloth[1]].append(cloth[0])
        else:
            cloth_group_by[cloth[1]] = [cloth[0]]

    answer = 1
    for key in cloth_group_by:
        answer = (len(cloth_group_by[key]) + 1) * answer

    answer -= 1
    return answer


print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
