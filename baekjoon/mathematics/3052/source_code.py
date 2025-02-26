"""
n_list = [int(input()) for _ in range(10)]
remainder_list = []
is_existed = [False] * 42
count = 0

for i in range(10):
    remainder_list.append(n_list[i] % 42)

for i in range(10):
    for j in range(42):
        if remainder_list[i] == j:
            is_existed[j] = True

for i in range(42):
    if is_existed[i] == True:
        count += 1

print(count)
"""

n_list = [int(input()) for _ in range(10)]
remainder_set = set()

for i in range(10):
    remainder_set.add(n_list[i] % 42)

print(len(remainder_set))