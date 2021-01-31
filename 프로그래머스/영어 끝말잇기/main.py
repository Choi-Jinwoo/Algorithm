def solution(n, words: list):
    for i in range(len(words)):
        if i != 0:
            if words[i - 1][-1] != words[i][0]:
                return [i % n + 1, i // n + 1]

        if words[i] in words[:i]:
            return [i % n + 1, i // n + 1]

    return [0, 0]


print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))
