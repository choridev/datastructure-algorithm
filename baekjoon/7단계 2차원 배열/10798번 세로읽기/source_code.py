string = []

for i in range(5):
    string.append(input())

for j in range(15):
    for i in range(5):
        if j < len(string[i]):
            print(string[i][j], end="")