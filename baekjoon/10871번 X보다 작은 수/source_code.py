N, X = map(int, input().split())

num_array = list(map(int, input().split()))

for i in range(N):
    if X > num_array[i]:
        print(num_array[i], end=" ")