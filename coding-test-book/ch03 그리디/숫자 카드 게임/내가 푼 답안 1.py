import sys

# n은 행의 개수, m은 열의 개수
n, m = map(int, sys.stdin.readline().rstrip().split())
# 숫자 카드를 저장할 2차원 리스트
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

# 각 행에서 가장 작은 숫자를 찾기
min_list = [min(array) for array in matrix]
# 작은 숫자들 중에서 가장 큰 것을 선택
result = max(min_list)

print(result)