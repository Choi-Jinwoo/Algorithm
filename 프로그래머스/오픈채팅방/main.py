from enum import Enum


class Action(Enum):
    Enter = 'Enter'
    Leave = 'Leave'


def analysis_message(message: str):
    data = message.split(' ')
    print(data)
    str_action, user_id, nickname = data

    if str_action == Action.Enter:
        return Action.Enter, user_id, nickname

    return Action.Leave, user_id, nickname


def solution(record):
    answer = []
    logs = []

    for r in record:
        logs.append(analysis_message(r))

    print(logs)

    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
