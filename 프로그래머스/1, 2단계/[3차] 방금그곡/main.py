def replace_code(s):
    dic = {
        'C#': '1',
        'D#': '2',
        'F#': '3',
        'G#': '4',
        'A#': '5',
        'E#': '6'
    }

    result = ''
    for i in range(len(s)):
        if s[i] == '#':
            continue

        if len(s) - 1 > i and s[i + 1] == '#':
            result += dic[s[i] + '#']
        else:
            result += s[i]

    return result


def calc_time(start, end):
    hour = int(end[0] + end[1]) - int(start[0] + start[1])
    minute = int(end[3] + end[4]) - int(start[3] + start[4])

    return hour * 60 + minute


def solution(m, musicinfos):
    musics = []

    for musicinfo in musicinfos:
        start, end, name, code = musicinfo.split(',')
        time = calc_time(start, end)
        code = replace_code(code)
        if time <= len(code):
            musics.append((time, name, code[:time]))
        else:
            code = code * (time // len(code) + 1)
            musics.append((time, name, code[:time]))

    result_music = None
    m = replace_code(m)
    for music in musics:
        time, name, code = music
        if m in code and result_music is None:
            result_music = music
        elif m in code and result_music[0] < music[0]:
            result_music = music

    if result_music is None:
        return '(None)'

    return result_music[1]
