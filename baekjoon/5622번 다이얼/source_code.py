alphabet = input()
time = 0

for i in range(len(alphabet)):
    target = alphabet[i]
    if target in "ABC":
        time += 3
    elif target in "DEF":
        time += 4
    elif target in "GHI":
        time += 5
    elif target in "JKL":
        time += 6
    elif target in "MNO":
        time += 7
    elif target in "PQRS":
        time += 8
    elif target in "TUV":
        time += 9
    elif target in "WXYZ":
        time += 10

print(time)