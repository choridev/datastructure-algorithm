A, B, V = map(int, input().split())

# distance = 0
# for i in range(1, V + 1):
#     distance += A
#     print(distance)
#     if distance >= V:
#         print(i)
#         break
#     else:
#         distance -= B

# """
# 올라가는 것과 미끄러지는 것의 간격을 몇 번 반복하면
# 마지막에 올라가는 것을 제외한 높이에
# 처음으로 도달할 수 있는지 계산
# """
# interval = A - B
# quotient = (V - A) // interval
# remainder = (V - A) % interval

# if remainder == 0:
#     print(quotient + 1)
# else:
#     print(quotient + 2)

"""math 모듈의 ceil()을 사용하여 올림"""
import math

interval = A - B
quotient = math.ceil((V - A) / interval)

print(quotient + 1)