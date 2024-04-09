N = int(input())
int_list = list(map(int, input().split()))
v = int(input())

# count = 0
# for i in range(N):
#     if int_list[i] == v:
#         count += 1
# print(count)

print(int_list.count(v))