a, b, c = map(int, input().split())

if a == b and a == c:
    print(10000 + a * 1000)
elif (a == b and a != c) or (a != b and a == c):
    print(1000 + 100 * a)
elif (b == c and b != a):
    print(1000 + 100 * b)
else:
    if a > b:
        if a > c:
            print(a * 100)
        else:
            print(c * 100)
    else:
        if b > c:
            print(b * 100)
        else:
            print(c * 100)