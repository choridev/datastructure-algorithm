import sys

input = sys.stdin.readline

n, k = map(int, input().split())
kind = [int(input().rstrip()) for _ in range(n)]
count = [0] * n

kind.sort(reverse=True)

remainder = k
for i in kind:
    quotient, remainder = divmod(remainder, i)
    count.append(quotient)

print(sum(count))
