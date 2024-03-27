count_subject = int(input())
subject_score = list(map(int, input().split()))
max_score = -1
sum = 0

for i in range(count_subject):
    if  subject_score[i] > max_score:
        max_score = subject_score[i]

for i in range(count_subject):
    sum += subject_score[i] / max_score * 100

print(sum / count_subject)