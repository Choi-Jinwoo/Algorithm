
def solution(priorities, location):
    priorities_dict = []
    for i, p in enumerate(priorities):
        p_dic = {
            'value': p,
            'location': i,
        }
        priorities_dict.append(p_dic)

    result = 0
    while len(priorities_dict) != 0:
        doc = priorities_dict[0]

        max_n = 0
        for p_d in priorities_dict:
            if max_n < p_d['value']:
                max_n = p_d['value']

        if max_n <= doc['value']:
            result += 1
            priorities_dict = priorities_dict[1:]

            if location == doc['location']:
                break
        else:
            priorities_dict = priorities_dict[1:]
            priorities_dict.append(doc)

    return result


solution([1,1,9,1,1,1], 0)