import itertools


def solution(orders, course):
    menus = []
    [menus.append(menu) for order in orders for menu in order if menu not in menus]
    menus.sort()

    result = []

    for course_len in course:
        store = {}
        for order in orders:
            combs = list(map(''.join, list(itertools.combinations(order, course_len))))
            for comb in combs:
                comb = ''.join(sorted(comb))
                if comb in store:
                    store[comb] += 1
                else:
                    store[comb] = 1

        max_cnt = 0
        course = []

        for item in store.items():
            key, value = item
            if value > 1:
                if value > max_cnt:
                    max_cnt = value
                    course = [key]
                elif value == max_cnt:
                    course.append(key)

        result.extend(course)

    return sorted(result)


print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
