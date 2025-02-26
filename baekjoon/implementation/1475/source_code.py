import math

N = input()
numbers = [0 for _ in range(10)]

for i in N:
    numbers[int(i)] += 1

required_6_9 = math.ceil((numbers[6] + numbers[9]) / 2)
del numbers[9]
del numbers[6]

if max(numbers) > required_6_9:
    print(max(numbers))
else:
    print(required_6_9)