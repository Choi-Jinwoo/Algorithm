def solution(n):
    char_map = ['', '1', '2', '4']
    div, mod = divmod(n, 3)

    result = ''

    while True:
        if mod == 0:
            div -= 1
            mod = 3

        result += char_map[mod]

        if div < 3:
            result += char_map[div]
            break

        div, mod = divmod(div, 3)

    return ''.join(reversed(result))


solution(1000)
