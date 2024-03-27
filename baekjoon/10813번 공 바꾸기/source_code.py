N, M = map(int, input().split())
box = [x for x in range(1, N + 1)]

# for y in range(M):
#     i, j = map(int, input().split())
#     tmp = box[i - 1]
#     box[i - 1] = box[j - 1]
#     box[j - 1] = tmp

for y in range(M):
    i, j = map(int, input().split())
    box[i - 1], box[j - 1] = box[j - 1], box[i - 1]

for y in range(N):
    print(box[y], end=" ")