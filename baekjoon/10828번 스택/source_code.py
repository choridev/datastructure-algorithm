import sys

def input():
    return sys.stdin.readline().rstrip()

stack = []

def size():
    return len(stack)

def empty():
    if size() == 0:
        return 1
    else:
        return 0

def push(data):
    stack.append(data)

def pop():
    if empty() == 1:
        data = -1
    else:
        data = stack.pop()
    return data

def top():
    if empty() == 1:
        data = -1
    else:
        data = stack[-1]
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
    elif instruction == 'top':
        print(top())
    else:
        instruction, data = instruction.split()
        push(data)