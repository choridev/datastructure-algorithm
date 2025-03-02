import sys

input = sys.stdin.readline

n = int(input())
result = 0

for i in range(1, n):
    total = 0
    seven, remainder = divmod(i, 1000000)
    six, remainder = divmod(remainder, 100000)
    five, remainder = divmod(remainder, 10000)
    four, remainder = divmod(remainder, 1000)
    three, remainder = divmod(remainder, 100)
    two, one = divmod(remainder, 10)
    total = i + seven + six + five + four + three + two + one

    if total == n:
        result = i
        break

print(result)
