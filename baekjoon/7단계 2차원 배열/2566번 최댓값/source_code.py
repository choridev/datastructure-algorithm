matrix = []
max = 0
row = 0
column = 0

for i in range(9):
    matrix.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if matrix[i][j] >= max:
            max = matrix[i][j]
            row = i + 1
            column = j + 1

print(max)
print(row, column)