N, K = map(int, input().split())
count = 0

for i in range(1, N + 1):
    remainder = N % i
    if remainder == 0:
        count += 1
        if count == K:
            print(i)
if count < K:
    print(0)