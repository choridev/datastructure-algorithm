H, M = map(int, input().split())

if M >=45:
    M -= 45
elif H != 0 and M < 45:
    H -= 1
    M += 15
else:
    H = 23
    M += 15

print("%d %d" % (H, M))