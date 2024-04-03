N, B = map(int, input().split())
converted_num = []

flag = True
while flag:
    remainder = N % B
    if len(converted_num) == 0:
        converted_num.append(remainder)
    else:
        converted_num.insert(0, remainder)
    N //= B
    if N < B:
        if N != 0:
            converted_num.insert(0, N)
        flag = False

for i in range(len(converted_num)):
    if converted_num[i] >= 10:
        print(chr(converted_num[i] + 55), end="")
    else:
        print(converted_num[i], end="")