# 최소공약수 알고리즘
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
for i in range(n + 1):
    print('o' * (n - i) + 'x' * i)
