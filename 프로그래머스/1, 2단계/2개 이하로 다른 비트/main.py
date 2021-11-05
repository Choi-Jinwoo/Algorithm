def solution(numbers):
    b_numbers = []
    for number in numbers:
        b_number = format(number, 'b')
        if len(b_number) == b_number.count('1'):
            b_number = '1' + b_number
            if len(b_number) > 1:
                b_number = b_number[0] + '0' + b_number[2:]
        else:
            for i in range(len(b_number) - 1, -1, -1):
                if b_number[i] == '0':
                    if i + 1 < len(b_number):
                        b_number = b_number[:i] + '10' + b_number[i + 2:]
                    else:
                        b_number = b_number[:i] + '1' + b_number[i + 1:]
                    break
        b_numbers.append(b_number)

    return list(map(lambda x: int(x, 2), b_numbers))


print(solution([17]))
