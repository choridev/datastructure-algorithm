import sys
from collections import deque

input = sys.stdin.readline
steps = ((-1, 0), (1, 0), (0, -1), (0, 1))

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
count = [[0] * m for _ in range(n)]

def bfs():
    q = deque()
    graph[0][0] = 0
    count[0][0] = 1
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0:
                graph[nx][ny] = 0
                count[nx][ny] = count[x][y] + 1
                q.append((nx, ny))
                if nx == (n - 1) and ny == (m - 1):
                    return

bfs()
print(count[n - 1][m - 1])
