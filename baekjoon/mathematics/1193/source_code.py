# 1번 line: 합 2, X 1, 개수 1개, 누적 1개
# 2번 line: 합 3, X 2~3, 개수 2개, 누적 3개
# 3번 line: 합 4, X 4~6, 개수 3개, 누적 6개
# 4번 line: 합 5, X 7~10, 개수 4개,  누적 10개

# 홀수 line: 왼쪽 위에서 오른쪽 위로 이동
# 짝수 line: 오른쪽 위에서 왼쪽 아래로 이동

X = int(input())
line = 0
max = 0
min = 0

for line in range(1, X + 1):
    max += line
    min = max - line + 1
    if min <= X and X <=  max:
        break

if line % 2 == 1:
    numerator = line
    denominator = 1
    for i in range(min, max + 1):
        if X == i:
            print("%d/%d" %(numerator, denominator))
            break
        numerator -= 1
        denominator += 1
else:
    numerator = 1
    denominator = line
    for i in range(min, max + 1):
        if X == i:
            print("%d/%d" %(numerator, denominator))
            break
        numerator += 1
        denominator -= 1