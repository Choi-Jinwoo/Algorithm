def solution(numbers):
    str_numbers = list(map(str, numbers))

    str_numbers.sort(reverse=True)

    for j in range(len(str_numbers)):
        for i in range(len(str_numbers) - 1):
            if str_numbers[i + 1] == str_numbers[i][:-1] and str_numbers[i][-1] < str_numbers[i + 1][-1]:
                str_numbers[i], str_numbers[i + 1] = str_numbers[i + 1], str_numbers[i]

    print(str_numbers)
    print(''.join(str_numbers))


solution([3, 302, 34, 5, 9, 30])
