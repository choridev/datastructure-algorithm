n_list = [int(input()) for _ in range(9)]
max_num = n_list[0]

print(max(n_list))
print(n_list.index(max(n_list)) + 1)