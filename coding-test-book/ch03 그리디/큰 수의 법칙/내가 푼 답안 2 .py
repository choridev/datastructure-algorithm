import sys

# n: 배열의 크기, m: 더하는 횟수, k: 특정 인덱스의 수를 연속해서 더할 수 있는 횟수
n, m, k = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

first = max(array) # 가장 큰 수
array.remove(first)
second = max(array) # 두 번째로 큰 수

sequence = first * k + second # 반복되는 수열

result = 0
result += sequence * (m // (k + 1))
result += first * (m % (k + 1))

print(result) # 최종 답안 출력