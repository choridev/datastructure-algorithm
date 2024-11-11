import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

queue = deque()

def size():
    return len(queue)

def empty():
    if size() == 0:
        return 1
    else:
        return 0

def push(data):
    queue.append(data)

def pop():
    if empty() == 1:
        data = -1
    else:
        data = queue.popleft()
    return data

def front():
    if empty() == 1:
        data = -1
    else:
        data = queue[0]
    return data

def back():
    if empty() == 1:
        data = -1
    else:
        data = queue[-1]
    return data

n = int(input())

for _ in range(n):
    instruction = input()
    if instruction == 'size':
        print(size())
    elif instruction == 'empty':
        print(empty())
    elif instruction == 'pop':
        print(pop())
    elif instruction == 'front':
        print(front())
    elif instruction == 'back':
        print(back())
    else:
        instruction, data = instruction.split()
        push(data)