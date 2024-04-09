N = int(input())
int_list = list(map(int, input().split()))

min = int_list[0]
max = int_list[0]

for i in range(1, N):
    if int_list[i] > max:
        max = int_list[i]
    if int_list[i] < min:
        min = int_list[i]

print(min, max)