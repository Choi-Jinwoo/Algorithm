def word_collection(word):
    words = []

    for i in range(0, len(word) - 1):
        created_word = word[i] + word[i + 1]
        if created_word.isalpha():
            words.append(created_word)

    return words


def solution(str1: str, str2: str):
    str1_collection = word_collection(str1.lower())
    str2_collection = word_collection(str2.lower())

    inter = []
    sum = []

    for c in str1_collection:
        if c in str2_collection:
            inter.append(c)
            str2_collection.remove(c)

        sum.append(c)

    sum.extend(str2_collection)

    if len(sum) == 0:
        return 65536

    return int(len(inter) / len(sum) * 65536)


print(solution('FRANCE', 'french'))
