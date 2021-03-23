def is_contains(container_list, arr):
    for container in container_list:
        print(container, arr)
        if container == arr:
            return False

        if container.find(arr) != -1:
            return True

    return False


def solution(orders, course):
    course_foods = []

    for i in range(len(orders) - 1):
        for j in range(i + 1, len(orders)):
            duplicate_foods = list(set(orders[i]) & set(orders[j]))
            duplicate_foods.sort()
            duplicate_foods = ''.join(duplicate_foods)

            if len(duplicate_foods) != 1 \
                    and len(duplicate_foods) in course:
                course_foods.append(duplicate_foods)

    result = []
    print(course_foods)
    for count in course:
        mostly_showed_food = {
            'count': 0,
            'food': [],
        }

        for food in course_foods:
            if len(food) == count and food not in mostly_showed_food['food']:
                if mostly_showed_food['count'] <= course_foods.count(food):
                    if mostly_showed_food['count'] < course_foods.count(food):
                        mostly_showed_food['food'] = []
                    mostly_showed_food['count'] = course_foods.count(food)
                    mostly_showed_food['food'].append(food)

        if mostly_showed_food['count'] > 0:
            result.extend(mostly_showed_food['food'])

    result.sort()
    return result


print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
