import sys

def hashfunc(sequence):
    result = 0
    for index, value in enumerate(sequence):
        result += (value * (31 ** index))
    result %= 1234567891
    return result

l = int(sys.stdin.readline().rstrip())
sequence = list(map(lambda x: ord(x) - 96, list(sys.stdin.readline().rstrip())))

print(hashfunc(sequence))