x, y, w, h = map(int, input().split())

way = []

way.append(h - y)
way.append(y - 0)
way.append(x - 0)
way.append(w - x)

print(min(way))