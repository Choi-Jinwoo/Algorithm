def solution(enroll: list, referral, seller, amount):
    tree = {}
    total_money = {}
    for i in range(0, len(enroll)):
        tree[enroll[i]] = referral[i]
        total_money[enroll[i]] = 0

    for i in range(0, len(seller)):
        money = amount[i] * 100

        curr_seller = seller[i]

        if tree[curr_seller] == '-':
            total_money[curr_seller] += (money - money // 10)
        else:
            while True:
                total_money[curr_seller] += (money - money // 10)
                money = money // 10

                if tree[curr_seller] == '-':
                    break

                curr_seller = tree[curr_seller]

    return list(total_money.values())
