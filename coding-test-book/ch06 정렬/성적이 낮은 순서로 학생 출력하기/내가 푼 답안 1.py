import sys

n = int(sys.stdin.readline().rstrip())
students = [sys.stdin.readline().rstrip().split() for _ in range(n)]

students.sort(key=lambda x: int(x[1]))

for student in students:
    print(student[0], end=' ')