N = int(input())
max_x = -10001
min_x = 10001
max_y = -10001
min_y = 10001

points = [list(map(int, input().split())) for _ in range(N)]

for i in points:
    if max_x < i[0]:
        max_x = i[0]
    if min_x > i[0]:
        min_x = i[0]
    if max_y < i[1]:
        max_y = i[1]
    if min_y > i[1]:
        min_y = i[1]

print((max_x - min_x) * (max_y - min_y))