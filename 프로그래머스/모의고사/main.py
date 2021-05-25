def solution(answers):
    a = [1, 2, 3, 4, 5] * 2500
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 2000
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 2000

    correct = [0, 0, 0]

    for answer, a_ans, b_ans, c_ans in zip(answers, a, b, c):
        if answer == a_ans:
            correct[0] += 1
        if answer == b_ans:
            correct[1] += 1
        if answer == c_ans:
            correct[2] += 1

    max_correct = max(correct)

    result = []
    for i in range(len(correct)):
        if correct[i] == max_correct:
            result.append(i + 1)

    return result

    # return [i + 1 for i in range(len(result)) if result[i] == return_value]


print(solution([3, 3]))
