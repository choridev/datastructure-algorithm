lines = list(map(int, input().split()))

max_line = max(lines)
min_line = min(lines)
middle_line = sum(lines) - max_line - min_line

while True:
    if max_line >= middle_line + min_line:
        max_line -= 1
    else:
        break

print(max_line + middle_line + min_line)