from itertools import combinations


def is_duplicate(wrapper, str):
    for c in str:
        if c not in wrapper:
            return False

    return True


def candidate_key(attrs, relation):
    candidate_keys = []

    row_len = len(relation)

    data_list = list(map(lambda row: '/'.join([row[attr] for attr in attrs]), relation))
    if len(set(data_list)) == row_len:
        candidate_keys.append(attrs)

    return candidate_keys


def solution(relation):
    candidate_keys = []
    cols_len = len(relation[0])
    combs = []
    for i in range(1, cols_len + 1):
        combs.extend(list(combinations(range(0, cols_len), i)))

    for comb in combs:
        keys = candidate_key(comb, relation)

        for key in keys:
            for c_key in candidate_keys:
                if is_duplicate(key, c_key):
                    break
            else:
                candidate_keys.append(key)

    return len(candidate_keys)


solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
          ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]])
