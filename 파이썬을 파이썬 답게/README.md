# 파이썬을 파이썬답게



### 몫과 나머지

```python
# divmod 메소드
print(divmod(1, 2))

# 결과
# (0, 2)
```



### N진법으로 표기된 string을 10진법 숫자로 변환하기

1번 풀이

```python
num = '3212'
base = 5

answer = 0
for idx, i in enumerate(num[::-1]):
	answer += int(i) * (base ** idx)
```

2번 풀이

```python
num = '3212'
base = 5
answer = int(num, base)
```



### 문자열 정렬하기

나의 풀이

```python
s, n = input().strip().split(' ')

n = int(n)

print(s)
print(' ' * ((n - len(s)) // 2), end = '')
print(s)
print(' ' * (n - len(s)), end = '')
print(s)
```

풀이

```python
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬
```



### 알파벳 출력하기

```python
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789
```



### 원본을 유지한채 정렬된 리스트 구하기

깊은 복사 풀이

```python
list1 = [3, 2, 1]
list2 = [i for i in list1] # 또는 copy.deepcopy를 사용
list2.sort()
```

sorted 풀이

```python
list1 = [3, 2, 1]
list2 = sorted(list1)
```



### 이차원 배열 뒤집기

zip 풀이

```python
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))
```

zip 사용 예시

```python
mylist = [ 1,2,3 ]
new_list = [ 40, 50, 60 ]
for i in zip(mylist, new_list):
    print (i)

# 결과
# (1, 40)
# (2, 50)
# (3, 60)
```



### 모든 멤버의 type 변환하기

map 풀이

```python
list1 = ['1', '100', '33']
list2 = list(map(int, list1))
```

map 사용 예시

```python
# 각 요소의 길이 리스트
list1 = ['1234', '12', '12345']
list2 = map(len, list2)
```

