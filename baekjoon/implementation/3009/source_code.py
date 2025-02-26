x_points = []
y_points = []

for i in range(3):
    x, y = map(int, input().split())
    if x in x_points:
        x_points.remove(x)
    else:
        x_points.append(x)
    if y in y_points:
        y_points.remove(y)
    else:
        y_points.append(y)

print(x_points[0], y_points[0])

