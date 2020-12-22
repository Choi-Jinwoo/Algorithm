# 피보나치 수를 재귀함수가 아닌 while 구문을 통해 계산함(StackOverflow 발생)

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibo(n - 1) + fibo(n - 2)


def solution(n):
    result = 0
    a = 1  # fibo(1)의 값으로 초기화(fibo(n - 1))
    b = 0  # fibo(n - 2)의 값
    i = 1

    while i < n:
        result = a + b

    return result


if __name__ == "__main__":
    print(solution(5))
