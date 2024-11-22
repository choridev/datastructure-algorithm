import sys

def input():
    return sys.stdin.readline().rstrip()

# 화폐의 종류 n
n, m = map(int, input().split())
# 화폐의 가치
array = [int(input()) for _ in range(n)]

# 다이나믹 프로그래밍 테이블
d = [10001] * (m + 1)
d[0] = 0

for i in array:
    for j in range(1, m + 1):
        if j % i == 0:
            d[j] = min(d[j], d[j - i] + 1)

print(d[m] if d[m] != 10001 else -1)