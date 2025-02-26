N = int(input())

for i in range(1, N + 1):
    print(" " * (N - i) + "*" * (2 * i - 1))
for i in range(1, N):
    print(" " * i + "*" * (2 * (N - i) - 1))

# for i in range(N):
#     for j in range(N - 1, i, -1):
#         print(" ", end="")
#     for k in range(2 * i + 1):
#         print("*", end="")
#     print()
# for i in range(N - 1):
#     for j in range(i + 1):
#         print(" ", end="")
#     for k in range(2 * (N - 1), 2 * i + 1, -1):
#         print("*", end="")
#     print()
