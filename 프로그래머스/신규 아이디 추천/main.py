usable_char = ['-', '_', '.']


def delete_exclude_char(id: str):
    result = []
    for c in id:
        if c.isalpha() or c.isdigit():
            result.append(c)
        elif c in usable_char:
            result.append(c)

    return ''.join(result)


def merge_period(id: str):
    stack = []
    for i in range(len(id)):
        if len(stack) > 0 and stack[-1] == '.' and id[i] == '.':
            stack.pop()

        stack.append(id[i])

    if len(stack) > 0 and stack[0] == '.':
        del stack[0]

    if len(stack) > 0 and stack[-1] == '.':
        del stack[-1]

    return ''.join(stack)


def solution(new_id: str):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    new_id = delete_exclude_char(new_id)

    # 3,4단계
    new_id = merge_period(new_id)

    # 5단계
    if len(new_id) <= 0:
        new_id = 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]

    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 7단계
    if len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id = new_id + new_id[-1]

    return new_id
