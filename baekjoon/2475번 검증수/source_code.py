numbers = list(map(int, input().split()))

for i in range(5):
    numbers[i] = numbers[i] ** 2

print(sum(numbers) % 10)