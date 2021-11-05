def solution(s):
    stack = []
    for c in s:
        if len(stack) == 0 and c == ')':
            return False

        if c == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(c)

    if len(stack) == 0:
        return True

    return False


print(solution('())('))
