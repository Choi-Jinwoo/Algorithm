def analyze_message(message):
    return message.split(' ')


def compose_result_message(message_arr, nickname_map):
    action_type, user_id = message_arr

    if action_type == 'Enter':
        return f'{nickname_map[user_id]}님이 들어왔습니다.'
    elif action_type == 'Leave':
        return f'{nickname_map[user_id]}님이 나갔습니다.'


def solution(record):
    result_record = []
    nickname_map = {}
    for message in record:
        user_info = analyze_message(message)

        if user_info[0] == 'Change' or user_info[0] == 'Enter':
            nickname_map[user_info[1]] = user_info[2]

        if user_info[0] != 'Change':
            result_record.append([user_info[0], user_info[1]])

    return [compose_result_message(record, nickname_map) for record in result_record]


solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
