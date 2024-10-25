import sys

n = int(sys.stdin.readline().rstrip())
part_num = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
order_num = list(map(int, sys.stdin.readline().rstrip().split()))

part_num.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for num in order_num:
    if binary_search(part_num, num, 0, n - 1) is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')