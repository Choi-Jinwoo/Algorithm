def solution(phone_book):
    phone_book_dict = {}
    for phone_number in phone_book:
        phone_book_dict[phone_number] = 1

    for phone_number in phone_book:
        number_list = ''
        for number in phone_number:
            number_list += number
            if number_list in phone_book_dict and number != phone_number:
                return False

    return True

