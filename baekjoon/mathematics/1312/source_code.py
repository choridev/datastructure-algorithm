A, B, N = map(int, input().split())
quotient = 0

for i in range(N):
    A = (A % B) * 10
    quotient = A // B

print(quotient)