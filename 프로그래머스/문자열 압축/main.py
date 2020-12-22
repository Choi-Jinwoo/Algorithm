def solution(s):
    zipped = []

    raw_split_list = []
    for n in range(1, len(s)):
        str_list = []
        for i in range(0, len(s), n):
            str_list.append(s[i:i + n])

        raw_split_list.append(str_list)

    for str_list in raw_split_list:
        loop_str = str_list[0]
        post_str = ''
        cnt = 0

        if len(loop_str) != 1:
            for i in range(len(str_list)):
                if str_list[i] == loop_str:
                    cnt += 1
                else:
                    post_str = ''.join(str_list[i:])
                    break
            if cnt == 0:
                result = f'{loop_str}{post_str}'
            else:
                result = f'{cnt}{loop_str}{post_str}'
        else:
            result = s

        print(str_list, result)
        zipped.append(len(result))

    return min(zipped)



print(solution('aabbaccc'))
