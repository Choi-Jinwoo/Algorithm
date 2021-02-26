def solution(number: str, k: int):
    sorted_number = sorted(number, reverse=True)

    sorted_index = 0
    i = 0
    start_index = 0
    while True:
        while True:
            n_index = number.index(sorted_number[sorted_index])
            if n_index <= k:
                number = number[start_index:]
                k -= n_index
                break

            sorted_index += 1




solution("1924", 1)


