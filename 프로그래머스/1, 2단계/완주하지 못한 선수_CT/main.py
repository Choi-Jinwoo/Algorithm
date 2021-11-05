def solution(participant, completion):
    completion_dict = {}

    for c in completion:
        if c in completion_dict:
            completion_dict[c] += 1
        else:
            completion_dict[c] = 1

    for p in participant:
        if p in completion_dict:
            if completion_dict[p] == 0:
                return p

            completion_dict[p] -= 1
        else:
            return p


solution(["leo", "kiki", "eden"], ["eden", "kiki"])