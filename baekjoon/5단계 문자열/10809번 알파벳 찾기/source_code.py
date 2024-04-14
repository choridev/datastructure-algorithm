S = input()
alphabet = [-1] * 26

for i in range(97, 123):
    index = i - 97
    for j in range(len(S)):
        if alphabet[index] != -1:
            continue
        if S[j] == chr(i):
            alphabet[index] = j
    print(alphabet[index], end=" ")