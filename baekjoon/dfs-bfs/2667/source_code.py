import sys
from collections import deque
import pprint

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
counts = []

steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    global count
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

def bfs(x, y):
    global count
    q = deque()
    if graph[x][y] == 1:
        q.append((x, y))
        graph[x][y] = 0
        count += 1
        while q:
            now = q.popleft()
            for step in steps:
                nx = now[0] + step[0]
                ny = now[1] + step[1]
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0
                    count += 1
        return True
    return False
    
result = 0
count = 0
for i in range(n):
    for j in range(n):
        if bfs(i, j) == True:
            result += 1
            counts.append(count)
            count = 0

print(result)

counts.sort()
for i in counts:
    print(i)