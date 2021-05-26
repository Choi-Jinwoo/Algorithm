def solution(s):
    stack = []
    for c in s:
        if len(stack) <= 0:
            stack.append(c)
            continue

        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if len(stack) <= 0:
        return 1

    return 0

solution("abab")
