A, B = input().split()

A_100 = A[0]
A_10 = A[1]
A_1 = A[2]

B_100 = B[0]
B_10 = B[1]
B_1 = B[2]

A = int(A_1 + A_10 + A_100)
B = int(B_1 + B_10 + B_100)

if A > B:
    print(A)
else:
    print(B)