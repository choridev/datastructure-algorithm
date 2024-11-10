import sys

index = 0
num = 0
next_num = 0

for i in range(3):
    data = sys.stdin.readline().rstrip()
    if 'z' in data:
        continue
    else:
        index = i
        num = int(data)

if index == 0:
    next_num = num + 3
elif index == 1:
    next_num = num + 2
else:
    next_num = num + 1

if next_num % 15 == 0:
    print('FizzBuzz')
elif next_num % 3 == 0:
    print('Fizz')
elif next_num % 5 == 0:
    print('Buzz')
else:
    print(next_num)