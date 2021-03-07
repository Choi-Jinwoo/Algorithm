def solution(number: str, k):
    number_array = list(map(int, list(number)))

    del_cnt = 0

    i = 0
    stack = []
    while del_cnt < k:
        if i >= len(number_array):
            stack.pop()
            del_cnt += 1
        else:
            if len(stack) <= 0:
                stack.append(number_array[i])
                i += 1
            elif stack[-1] < number_array[i]:
                del_cnt += 1
                stack.pop()
                stack.append(number_array[i])
            else:
                stack.append(number_array[i])
                i += 1

    return ''.join(map(str, stack))


print(solution('4177252841', 4))
