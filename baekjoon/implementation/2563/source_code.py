white_paper = [[0 for _ in range(100)] for _ in range(100)]
black_paper_area = 0

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    for i in range(100):
        if x <= i <= x + 9:
            for j in range(100):
                if y <= j <= y + 9:
                    white_paper[i][j] = 1

for i in range(100):
        for j in range(100):
            if white_paper[i][j] == 1:
                black_paper_area += 1

print(black_paper_area)