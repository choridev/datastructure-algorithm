import sys

input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))
total = 0

times.sort(reverse=True)
for idx, val in enumerate(times):
    total += (idx + 1) * val

print(total)
