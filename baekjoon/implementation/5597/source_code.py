n_list = [n for n in range(1, 31)]

for i in range(28):
    student_id = int(input())
    n_list.remove(student_id)

print(n_list[0])
print(n_list[1])