hash_table = list(0 for i in range(10))


def hash_func(key):
    hash_key = hash(key)
    store_key = hash_key % 10
    return store_key


def store(key, value):
    index = hash_func(key)

    if hash_table[index] == 0:
        hash_table[index] = [key, value]
    else:
        for i in range(index + 1, len(hash_table)):
            if hash_table[i] == 0:
                hash_table[i] = [key, value]
                return
            elif hash_table[i][0] == index:
                hash_table[i][1] = value
                return


def get_value(key):
    index = hash_func(key)

    if hash_table[index] == 0:
        return None
    else:
        for i in range(index + 1, len(hash_table)):
            if hash_table[i] == 0:
                return None
            elif hash_table[i][0] == key:
                return hash_table[1][1]
    return None


print(hash_func('key1'))
print(hash_func('key2'))
print(hash_func('key3'))
print(hash_func('key4'))

store('key1', 'value1')
store('key2', 'value2')
store('key3', 'value3')
store('key4', 'value3')

print(hash_table)
