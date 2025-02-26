N, M = map(int, input().split())
box = [0] * N
# box = [0 for _ in range(N)]

for x in range(M):
    i, j, k = map(int, input().split())
    for y in range(i, j + 1):
        del(box[y - 1])
        box.insert(y - 1, k)

for x in range(N):
    print(box[x], end=" ")