import sys

n = int(sys.stdin.readline().rstrip())
array = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

array.sort()

for num in array:
    print(num)