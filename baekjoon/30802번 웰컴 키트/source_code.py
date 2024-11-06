import sys
import math

n = int(sys.stdin.readline().rstrip())
size = list(map(int, sys.stdin.readline().rstrip().split()))
t, p = map(int, sys.stdin.readline().rstrip().split())

shirt_bundle = 0
for i in size:
    shirt_bundle += math.ceil(i / t)

pen_bundle, pen_each = divmod(n, p)

print(shirt_bundle)
print(pen_bundle, pen_each)