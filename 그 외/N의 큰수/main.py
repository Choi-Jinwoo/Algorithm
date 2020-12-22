def sol(n):
    str_n_bin = bin(n)
    one_cont = str_n_bin.count('1')

    num = n + 1
    while True:
        str_num_bin = bin(num)
        num_one_count = str_num_bin.count('1')
        if num_one_count == one_cont:
            break

        num += 1

    return num


print(sol(78))

