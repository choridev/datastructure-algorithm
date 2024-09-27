import sys

# 나이트의 현재 위치 입력받기
location = list(sys.stdin.readline().rstrip())
init_x, init_y = location[0], int(location[1])

if init_x == 'a':
    init_x = 1
elif init_x == 'b':
    init_x = 2
elif init_x == 'c':
    init_x = 3
elif init_x == 'd':
    init_x = 4
elif init_x == 'e':
    init_x = 5
elif init_x == 'f':
    init_x = 6
elif init_x == 'g':
    init_x = 7
elif init_x == 'h':
    init_x = 8

# x, y는 나이트를 움직였을 때의 위치
x, y = init_x, init_y

count = 0

# 나이트를 8가지 방향으로 움직이면서 가능한 경우 세기
# 왼쪽으로 2번 이동
if (x := init_x - 2) >= 1:
    # 위쪽으로 1번 이동
    if (y := init_y - 1) >= 1:
        count += 1
    # 아래쪽으로 1번 이동
    if (y := init_y - 1) <= 8:
        count += 1

# 오른쪽으로 2번 이동
if (x := init_x + 2) <= 8:
    # 위쪽으로 1번 이동
    if (y := init_y - 1) >= 1:
        count += 1
    # 아래쪽으로 1번 이동
    if (y := init_y + 1) <= 8:
        count += 1

# 위쪽으로 2번 이동
if (y := init_y - 2) >= 1:
    # 왼쪽으로 1번 이동
    if (x := init_x - 1) >= 1:
        count += 1
    # 오른쪽으로 1번 이동
    if (x := init_x + 1) <= 8:
        count += 1

# 아래쪽으로 2번 이동
if (y := init_y + 2) >= 1:
    # 왼쪽으로 1번 이동
    if (x := init_x - 1) >= 1:
        count += 1
    # 오른쪽으로 1번 이동
    if (x := init_x + 2) <= 8:
        count += 1

print(count)