from itertools import permutations


def calc(order, expression):
    for op in order:
        stack = []
        i = 0
        while i < len(expression):
            if expression[i] == op and op == '+':
                stack[-1] = stack[-1] + expression[i + 1]
                i += 1
            elif expression[i] == op and op == '-':
                stack[-1] = stack[-1] - expression[i + 1]
                i += 1
            elif expression[i] == op and op == '*':
                stack[-1] = stack[-1] * expression[i + 1]
                i += 1
            else:
                stack.append(expression[i])
            i += 1

        expression = stack
    return expression[0]


def solution(expression):
    orders = list(permutations('*+-', 3))

    stack = []

    num = ''
    for c in expression:
        if c.isdigit():
            num += c
        else:
            stack.extend([int(num), c])
            num = ''
    stack.append(int(num))

    results = []
    for order in orders:
        results.append(abs(calc(order, stack.copy())))

    return max(results)


solution("100-200*300-500+20")
