while True:
    line = list(map(int, input().split()))

    max_num = max(line)
    min_num = min(line)
    middle_num = sum(line) - max_num - min_num

    if max_num == 0 and middle_num == 0 and min_num == 0:
        break
    elif max_num >= middle_num + min_num:
        print("Invalid")
    elif max_num == middle_num and max_num == min_num and middle_num == min_num:
        print("Equilateral")
    elif max_num != middle_num and max_num != min_num and middle_num != min_num:
        print("Scalene")
    else:
        print("Isosceles")