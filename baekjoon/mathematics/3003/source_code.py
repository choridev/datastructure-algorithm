black_pieces = [1, 1, 2, 2, 2, 8]
white_pieces = list(map(int, input().split()))

for i in range(6):
    print(black_pieces[i] - white_pieces[i], end=" ")