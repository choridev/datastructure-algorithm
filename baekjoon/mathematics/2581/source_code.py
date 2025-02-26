M = int(input())
N = int(input())

prime_num = []
sum = 0

for i in range(M, N + 1):
    if i == 1:
        continue
    divisor_count = 0
    for j in range(2, i):
        if i % j == 0:
            divisor_count += 1
            break
    if divisor_count == 0:
        prime_num.append(i)

if len(prime_num) != 0:
    for i in prime_num:
        sum += i
    print(sum)
    print(prime_num[0])
else:
    print(-1)