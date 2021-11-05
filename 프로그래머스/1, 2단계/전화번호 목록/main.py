def solution(phone_book):
    for phone in phone_book:
        for target in phone_book:
            if target.find(phone) == 0 and target != phone:
                return False

    return True
