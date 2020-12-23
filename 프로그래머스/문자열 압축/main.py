def solution(s):
    zipped = []

    raw_split_list = []
    for n in range(1, len(s)):
        str_list = []
        for i in range(0, len(s), n):
            str_list.append(s[i:i + n])

        raw_split_list.append(str_list)

    for split_str in raw_split_list:
        loop_str = split_str[0]
        zip_result = ''
        cnt = 0
        for i in range(len(split_str)):
            if split_str[i] == loop_str:
                cnt += 1

            if i == len(split_str) - 1:
                if cnt == 1:
                    zip_result = f'{zip_result}{loop_str}'
                else:
                    zip_result = f'{zip_result}{cnt}{loop_str}'
                break

            if split_str[i + 1] != loop_str:
                if cnt == 1:
                    zip_result = f'{zip_result}{loop_str}'
                else:
                    zip_result = f'{zip_result}{cnt}{loop_str}'
                loop_str = split_str[i + 1]
                cnt = 0

        zipped.append(len(zip_result))

    if len(zipped) == 0:
        return 1

    return min(zipped)
