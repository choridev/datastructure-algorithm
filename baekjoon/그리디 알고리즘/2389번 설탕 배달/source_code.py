import sys

input = sys.stdin.readline

n = int(input())
optimal_five = 0
optimal_three = 0

max_five = n // 5 or 1
remainder = 0
for i in range(max_five, 0, -1):
    if (n - (5 * i)) % 3 == 0:
        optimal_five = i
        remainder = n - (5 * optimal_five)
        optimal_three = remainder // 3
        break
    else:
        if n % 3 == 0:
            optimal_three = n // 3

result = optimal_five + optimal_three
if result == 0:
    print(-1)
else:
    print(result)
