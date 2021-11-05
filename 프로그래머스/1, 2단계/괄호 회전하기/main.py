def rotate(s, n):
    return s[n:] + s[:n]


def solution(s):
    cnt = 0

    for i in range(len(s)):
        rotated = rotate(s, i)

        stack = []
        for c in rotated:
            if len(stack) <= 0:
                stack.append(c)
                continue

            if c == ')' and stack[-1] == '(':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)

        if len(stack) == 0:
            cnt += 1

    return cnt


print(solution('[](){}'))
