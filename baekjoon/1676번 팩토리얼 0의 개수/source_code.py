import sys

n = int(sys.stdin.readline().rstrip())

result = 1
for i in range(1, n + 1):
    result *= i

str_result = str(result)[::-1]

count = 0
for i in str_result:
    if i == '0':
        count += 1
    else:
        break

print(count)