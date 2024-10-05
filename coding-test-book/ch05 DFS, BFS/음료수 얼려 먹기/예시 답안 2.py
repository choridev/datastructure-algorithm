import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    if graph[x][y] == 1:
        return False
    
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        graph[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= (n - 1) and 0 <= ny <= (m - 1) and graph[nx][ny] == 0:
                queue.append((nx, ny))
    return True

result = 0
for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            result += 1

print(result)