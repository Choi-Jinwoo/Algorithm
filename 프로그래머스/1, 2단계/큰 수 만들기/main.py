def solution(number, k):
    stack = []

    cnt = 0
    i = 0
    while i < len(number):
        if len(stack) <= 0 or cnt >= k:
            stack.append(number[i])
            i += 1
            continue

        if len(number) - i <= k - cnt:
            print(stack, number[i])
            if stack[-1] >= number[i]:
                i += 1
                continue
            else:
                stack.pop()
                stack.append(number[i])
                i += 1
                continue

        if stack[-1] < number[i]:
            stack.pop()
            cnt += 1
        else:
            stack.append(number[i])
            i += 1

    return ''.join(stack)


print(solution('11119', 2))
