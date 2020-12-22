n = 10
b = 3

result = ''

while n > b:
    result += str(n % b)
    n //= b

result += str(n % b)
result += str(n // b)

if result[0] == '0':
    result = result[1:]

print(result)
result = result.replace('2', '4')
result = result.replace('1', '2')
result = result.replace('0', '1')

print(result)