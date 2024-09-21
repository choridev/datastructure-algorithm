import sys

# n은 행의 개수, m은 열의 개수
n, m = map(int, sys.stdin.readline().rstrip().split())

# 각 행에서 가장 작은 숫자를 저장
min_list = [min(list(map(int, sys.stdin.readline().rstrip().split()))) for _ in range(n)]

# 작은 숫자들 중에서 가장 큰 것을 선택
result = max(min_list)

print(result)