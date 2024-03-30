word = input()
count = [0] * 26
max = 0
max_index = 0
max_count = 0

# for i in range(len(word)):
#     if word[i] == 'A' or word[i] == 'a':
#         count[0] += 1
#     elif word[i] == 'B' or word[i] == 'b':
#         count[1] += 1
#     elif word[i] == 'C' or word[i] == 'c':
#         count[2] += 1
#     elif word[i] == 'D' or word[i] == 'd':
#         count[3] += 1
#     elif word[i] == 'E' or word[i] == 'e':
#         count[4] += 1
#     elif word[i] == 'F' or word[i] == 'f':
#         count[5] += 1
#     elif word[i] == 'G' or word[i] == 'g':
#         count[6] += 1
#     elif word[i] == 'H' or word[i] == 'h':
#         count[7] += 1
#     elif word[i] == 'I' or word[i] == 'i':
#         count[8] += 1
#     elif word[i] == 'J' or word[i] == 'j':
#         count[9] += 1
#     elif word[i] == 'K' or word[i] == 'k':
#         count[10] += 1
#     elif word[i] == 'L' or word[i] == 'l':
#         count[11] += 1
#     elif word[i] == 'M' or word[i] == 'm':
#         count[12] += 1
#     elif word[i] == 'N' or word[i] == 'n':
#         count[13] += 1
#     elif word[i] == 'O' or word[i] == 'o':
#         count[14] += 1
#     elif word[i] == 'P' or word[i] == 'p':
#         count[15] += 1
#     elif word[i] == 'Q' or word[i] == 'q':
#         count[16] += 1
#     elif word[i] == 'R' or word[i] == 'r':
#         count[17] += 1
#     elif word[i] == 'S' or word[i] == 's':
#         count[18] += 1
#     elif word[i] == 'T' or word[i] == 't':
#         count[19] += 1
#     elif word[i] == 'U' or word[i] == 'u':
#         count[20] += 1
#     elif word[i] == 'V' or word[i] == 'v':
#         count[21] += 1
#     elif word[i] == 'W' or word[i] == 'w':
#         count[22] += 1
#     elif word[i] == 'X' or word[i] == 'x':
#         count[23] += 1
#     elif word[i] == 'Y' or word[i] == 'y':
#         count[24] += 1
#     else:
#         count[25] += 1

for i in range(len(word)):
    match word[i]:
        case 'A' | 'a':
            count[0] += 1
        case 'B' | 'b':
            count[1] += 1
        case 'C' | 'c':
            count[2] += 1
        case 'D' | 'd':
            count[3] += 1
        case 'E' | 'e':
            count[4] += 1
        case 'F' | 'f':
            count[5] += 1
        case 'G' | 'g':
            count[6] += 1
        case 'H' | 'h':
            count[7] += 1
        case 'I' | 'i':
            count[8] += 1
        case 'J' | 'j':
            count[9] += 1
        case 'K' | 'k':
            count[10] += 1
        case 'L' | 'l':
            count[11] += 1
        case 'M' | 'm':
            count[12] += 1
        case 'N' | 'n':
            count[13] += 1
        case 'O' | 'o':
            count[14] += 1
        case 'P' | 'p':
            count[15] += 1
        case 'Q' | 'q':
            count[16] += 1
        case 'R' | 'r':
            count[17] += 1
        case 'S' | 's':
            count[18] += 1
        case 'T' | 't':
            count[19] += 1
        case 'U' | 'u':
            count[20] += 1
        case 'V' | 'v':
            count[21] += 1
        case 'W' | 'w':
            count[22] += 1
        case 'X' | 'x':
            count[23] += 1
        case 'Y' | 'y':
            count[24] += 1
        case 'Z' | 'z':
            count[25] += 1

for i in range(26):
    if count[i] > max:
        max = count[i]
        max_index = i
        max_count = 1
    elif count[i] == max:
        max_count += 1

if max_count > 1:
    print("?")
else:
    print(chr(max_index + 65))