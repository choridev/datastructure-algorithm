def plus_mul_minus(A, B):
    return (A + B) * (A - B)

A, B = map(int, input().split())

print(plus_mul_minus(A, B))