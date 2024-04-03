dex = 0
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = input().split()
B = int(B)

for i in range(len(N)):
    index = -(i + 1)
    if N[index] in alphabet:
        dex += (ord(N[index]) - 55) * B ** i
    else:
        dex += int(N[index]) * B ** i
print(dex)