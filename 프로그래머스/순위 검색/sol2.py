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


def count_filter_member(members, q):
    cnt = 0
    min_index = int(q[4]) // 10

    for key in members.keys():
        if int(key) < min_index:
            break

        member_arr = []
        if q[0] == '-':
            member_arr = members[key]['java'] + members[key]['python'] + members[key]['cpp']
        else:
            member_arr = members[key][q[0]]

        for member in member_arr:
            if (member[1] == q[1] or q[1] == '-') \
                    and (member[2] == q[2] or q[2] == '-') \
                    and (member[3] == q[3] or q[3] == '-') \
                    and member[4] >= int(q[4]):
                cnt += 1

    return cnt


def solution(info, query):
    members = {}

    for i in range(len(info)):
        member_info = info[i].split(' ')
        member_info[4] = int(member_info[4])

        if str(member_info[4] // 10) in members:
            members[str(member_info[4] // 10)][member_info[0]].append(member_info)
        else:
            members[str(member_info[4] // 10)] = {
                'java': [],
                'python': [],
                'cpp': [],
            }
            members[str(member_info[4] // 10)][member_info[0]].append(member_info)

    members = dict(sorted(members.items(), key=lambda x: int(x[0]), reverse=True))

    cnt_arr = []
    exit_query = {}

    for q in query:
        if q in exit_query:
            cnt_arr.append(exit_query[q])
        else:
            q_arr = split_query(q)
            cnt = count_filter_member(members, q_arr)
            cnt_arr.append(cnt)
            exit_query[q] = cnt

    return cnt_arr


import time

start = time.time()  # 시작 시간 저장

# 작업 코드
print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"] * 2000,
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"] * 500))

print("time :", time.time() - start)  # 현재시각 - 시작시간 =
