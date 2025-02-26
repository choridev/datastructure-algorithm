A = int(input())
B = int(input())
C = int(input())

value = A * B * C
value_list = list(str(value))

for i in range(10):
    print(value_list.count(str(i)))