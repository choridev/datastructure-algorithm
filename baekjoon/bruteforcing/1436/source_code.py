import sys

input = sys.stdin.readline

INF = int(1e9)
APOCALYPSE_NUMBER = '666'

n = int(input())

count = 0
for i in range(INF):
    if APOCALYPSE_NUMBER in str(i):
        count += 1
    if count == n:
        print(i)
        break
