import sys

# n은 연산을 통해 1로 만들어야 하는 수, k는 n의 배수일 때 나누는 수
n, k = map(int, sys.stdin.readline().rstrip().split())

result = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        n //= k
    else:
        n -= 1
    result += 1

print(result)