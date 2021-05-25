# round
def _round():
    print(round(12.34567, 2))  # 12.35


def _list():
    # 리스트 초기화
    arr = [0] * 10
    print(arr)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # list comprehension
    my_list = [1, 'hi', 2, 4, False]
    int_list = [x for x in my_list if type(x) == int]
    print(int_list)  # [2, 3, 5]

    # list method
    arr2 = []
    arr2.append(0)
    arr2.append(1)
    arr2.append(2)
    print(arr2)  # [2, 1, 0]
    arr2.sort()  # [0, 1, 2]
    arr2.insert(1, 2)
    print(arr2)  # [0, 2, 1, 2]
    print(arr2.count(2))  # 2
    arr2.remove(2)
    print(arr2)  # [0, 1, 2]


def _tuple():
    a = (1, 2, 3, 4)
    # a[0] = 0  compile error
    a = (0, 1, 2)
    print(a)  # (0, 1, 2)


def _dict():
    data = dict()
    data['java'] = '자바'
    data['cpp'] = 'c++'
    data['python'] = '파이썬'
    print(data.keys())  # dict_keys(['java', 'cpp', 'python'])
    print(data.values())  # dict_values(['자바', 'c++', '파이썬'])
    del data['cpp']
    print(data)  # {'java': '자바', 'python': '파이썬'}
    print(list(data))  # ['java', 'python']
    print(sorted(data))  # ['java', 'python']
    print('js' in data)  # False


def _set():
    a = {1, 2, 4, 5}
    b = {1, 3, 5}

    print(a | b)  # 함집합 {1, 2, 3, 4, 5}
    print(a & b)  # 교집합 {1, 5}
    print(a - b)  # 차집합 {2, 4}

    b.add(6)
    print(b)  # { 1, 3, 5, 6 }
    b.update([7, 8, 9])
    print(b)  # {1, 3, 5, 6, 7, 8, 9}
    b.remove(5)  # {1,3,6,7,8,9}
    print(b)


def _built_in_functions():
    arr = [1, 2, 3, 4, 5]
    print(sum(arr))  # 15
    print(min(arr))  # 1
    print(max(arr))  # 1

    a = {
        'apple': 2,
        'banana': 3,
        'melon': 1
    }
    result = sorted(a.items(), key=lambda x: x[1])
    print(result)  # [('melon', 1), ('apple', 2), ('banana', 3)]


_built_in_functions()


