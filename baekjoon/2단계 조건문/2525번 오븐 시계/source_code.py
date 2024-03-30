h, m = map(int, input().split())
cooking_minute = int(input())

# 현재 시각을 분으로 표시
now_to_minute = h * 60 + m

finish_minute = now_to_minute + cooking_minute

h = finish_minute // 60
m = finish_minute % 60

if h >= 24:
    h -= 24

print("%d %d" % (h, m))