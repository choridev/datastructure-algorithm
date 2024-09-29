import sys

n, m = map(int, sys.stdin.readline().split())
a, b, d = map(int, sys.stdin.readline().split())
world_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
player_map = [[-1] * m for _ in range(n)]

# 방향별 움직임
steps = ((-1, 0), (0, 1), (1, 0), (0, -1))

player_map[a][b] = 0


count = 1
turn_time = 0
while True:
    # 현재 방향을 기준으로 왼쪽 방향으로 회전
    d = d - 1 if d > 0 else 3
    na = a + steps[d][0]
    nb = b + steps[d][1]
    # 아직 가보지 않은 칸이면
    if player_map[na][nb] == -1:
        # 가본 방향의 수 초기화
        turn_time = 0
        # 이동하려는 곳이 육지면
        if world_map[na][nb] == 0:
            # 캐릭터가 가진 지도에 해당 위치를 육지로 표시
            player_map[na][nb] = 0
            # 캐릭터를 해당 위치로 이동
            a = na
            b = nb
            count += 1
        # 이동하려는 곳이 바다면
        else:
            # 캐릭터가 가진 지도에 해당 위치를 바다로 표시
            player_map[na][nb] = 1
    # 가본 칸이면
    else:
        # 가본 방향의 수 + 1
        turn_time += 1
        # 네 방향 모두 가보지 않았으면 다시 1단계로
        if turn_time < 4:
            continue
        # 네 방향 모두 가봤다면
        else:
            na = a - steps[d][0]
            nb = b - steps[d][1]
            # 가본 방향의 수 초기화
            turn_time = 0
            # 이동하려는 곳이 육지면
            if world_map[na][nb] == 0:
                # 캐릭터를 해당 위치로 이동
                a = na
                b = nb
            else:
                break

print(count)