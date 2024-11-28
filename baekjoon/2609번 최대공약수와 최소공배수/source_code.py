import sys
from math import gcd, lcm

def input():
    return sys.stdin.readline().rstrip()

num1, num2 = map(int, input().split())

# max_num = max(num1, num2)
# min_num = min(num1, num2)

# gcd = 0
# for i in range(max_num, 0, -1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i
#         break
# print(gcd)

# lcm = 0
# j = 1
# while True:
#     lcm = max_num * j
#     if lcm % min_num == 0:
#         break
#     j += 1
# print(lcm)

print(gcd(num1, num2))
print(lcm(num1, num2))