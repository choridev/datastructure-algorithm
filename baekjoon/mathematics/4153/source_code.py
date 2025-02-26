import sys

while (True):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    length = [a, b, c]
    
    if (a == 0 and b == 0 and c == 0):
        break

    length.sort()
    shortest, middle, longest = length
    
    if (longest ** 2) == (middle ** 2) + (shortest ** 2):
        print('right')
    else:
        print('wrong')