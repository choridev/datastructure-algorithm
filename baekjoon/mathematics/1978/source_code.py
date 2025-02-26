N = int(input())
input_num = list(map(int, input().split()))
prime_num_count = 0

for i in input_num:
    if i == 1:
        continue
    else:
        divisor_count = 0
        for j in range(2, i):
            if divisor_count >= 1:
                break
            if i % j == 0:
                divisor_count += 1
        if divisor_count == 0:
            prime_num_count += 1

print(prime_num_count)