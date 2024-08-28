T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    quotient, remainder = divmod(N, H)

    if remainder == 0:
        Y = H
        X = quotient
    else:
        Y = remainder
        X = quotient + 1

    Y = str(Y)
    X = '0' + str(X) if X < 10 else str(X)

    print(Y + X)