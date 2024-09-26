import sys

n = int(sys.stdin.readline().rstrip())
plans = (sys.stdin.readline().rstrip().split())
point = [1, 1]

for direction in plans:
    if direction == 'U':
        if point[0] != 1:
            point[0] -= 1
    elif direction == 'D':
        if point[0] != n:
            point[0] += 1
    elif direction == 'L':
        if point[1] != 1:
            point[1] -= 1
    elif direction == 'R':
        if point[1] != n:
            point[1] += 1

print(point[0], point[1])