import sys

input = sys.stdin.readline

n = int(input())
result = int(1e9)

quotient_of_five = n // 5

for count_of_five in range(quotient_of_five + 1):
    count = 0
    remainder_of_five = (n - (count_of_five * 5))
    remainder_of_three = remainder_of_five % 3
    if remainder_of_three == 0:
       quotient_of_three = remainder_of_five // 3 
       count = count_of_five + quotient_of_three
       if count < result:
           result = count

result = -1 if result == int(1e9) else result
print(result)
