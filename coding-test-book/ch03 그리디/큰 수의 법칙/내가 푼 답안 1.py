import sys

# n: 배열의 크기, m: 더하는 횟수, k: 특정 인덱스의 수를 연속해서 더할 수 있는 횟수
n, m, k = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

first = max(array) # 가장 큰 수
array.remove(first)
second = max(array) # 두 번째로 큰 수

result = 0
count = 0 # 가장 큰 수를 더한 횟수
for _ in range(m):
    if count < k:
        result += first
        count += 1
    else:
        result += second
        count = 0

print(result)