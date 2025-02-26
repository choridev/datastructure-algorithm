T = int(input())

for i in range(T):
    OX = input()

    score = 0
    combo = 0

    for i in OX:
        if i == 'O':
            combo += 1
            score += combo
        else:
            combo = 0

    print(score)