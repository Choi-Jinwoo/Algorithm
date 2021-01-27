# def split_query(query: str):
#     query = query.replace(' and', '')
#     return query.split(' ')
#
#
# def count_filter_member(info, q):
#     cnt = 0
#     for member in info:
#         if (member[0] == q[0] or q[0] == '-') \
#                 and (member[1] == q[1] or q[1] == '-') \
#                 and (member[2] == q[2] or q[2] == '-') \
#                 and (member[3] == q[3] or q[3] == '-') \
#                 and int(member[4]) >= int(q[4]):
#             cnt += 1
#
#     return cnt
#
#
# def solution(info, query):
#     info_arr = []
#     for member in info:
#         info_arr.append(member.split(' '))
#
#     cnt_arr = []
#     for q in query:
#         q_arr = split_query(q)
#         cnt_arr.append(count_filter_member(info_arr, q_arr))
#
#     return cnt_arr

################################### SOL 1 ###################################

def split_query(query: str):
    query = query.replace(' and', '')
    return query.split(' ')


def count_filter_member(lang, position, career, food, member_level, members, q):
    member_arr = []
    for key in member_level:
        if int(key) >= (int(q[4]) // 10):
            member_arr.extend(member_level[key])

    lang_arr = []
    position_arr = []
    career_arr = []
    food_arr = []
    member_level_arr = []

    if q[0] == '-':
        for val in lang.values():
            lang_arr.extend(val)
    else:
        lang_arr = lang[q[0]]

    if q[1] == '-':
        for val in position.values():
            position_arr.extend(val)
    else:
        position_arr = position[q[1]]

    if q[2] == '-':
        for val in career.values():
            career_arr.extend(val)
    else:
        career_arr = career[q[2]]

    if q[3] == '-':
        for val in food.values():
            food_arr.extend(val)
    else:
        food_arr = food[q[3]]

    for key in member_level:
        if int(key) >= (int(q[4]) // 10):
            member_level_arr.extend(member_level[key])

    print(lang_arr)
    print(position_arr)
    print(career_arr)
    print(food_arr)
    print(member_level_arr)
    result = set(lang_arr) & set(position_arr) & set(career_arr) & set(food_arr) & set(member_level_arr)
    print(result)
    print('-----')

    return len(result)


def solution(info, query):
    members = []

    lang = {}
    position = {}
    career = {}
    food = {}
    member_level = {}

    for i in range(len(info)):
        member_info = info[i].split(' ')
        member_info[4] = int(member_info[4])

        members.append(member_info)

        if member_info[0] in lang:
            lang[member_info[0]].append(i)
        else:
            lang[member_info[0]] = [i]

        if member_info[1] in position:
            position[member_info[1]].append(i)
        else:
            position[member_info[1]] = [i]

        if member_info[2] in career:
            career[member_info[2]].append(i)
        else:
            career[member_info[2]] = [i]

        if member_info[3] in food:
            food[member_info[3]].append(i)
        else:
            food[member_info[3]] = [i]

        member_level_key = str(member_info[4] // 10)
        if member_level_key in member_level:
            member_level[member_level_key].append(i)
        else:
            member_level[member_level_key] = [i]

    member_level = dict(sorted(member_level.items(), key=lambda x: int(x[0])))

    cnt_arr = []
    for q in query:
        q_arr = split_query(q)
        cnt_arr.append(count_filter_member(lang, position, career, food, member_level, members, q_arr))

    return cnt_arr


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
