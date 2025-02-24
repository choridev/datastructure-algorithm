import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    print(v, end=' ')
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i, end=' ')
    
dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)