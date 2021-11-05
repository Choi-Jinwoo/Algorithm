def is_balanced(s):
    return s.count('(') == s.count(')')


def is_correct(s):
    stack = []
    for c in s:
        if len(stack) <= 0:
            stack.append(c)
            continue

        if c == ')':
            stack.pop()
        else:
            stack.append(c)

    if len(stack) <= 0:
        return True

    return False


def convert(w):
    if len(w) <= 0:
        return ''

    u = ''
    v = ''

    for i in range(1, len(w)):
        if is_balanced(w[:i]):
            u = w[:i]
            v = w[i:]
            break
    else:
        u = w
        v = ''

    if is_correct(u):
        return u + convert(v)
    else:
        prefix = '(' + convert(v) + ')'

        u_result = ''
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                u_result += ')'
            else:
                u_result += '('
        return prefix + u_result


def solution(p):
    print(convert('()))((()'))


solution('')
