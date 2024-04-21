angle = [int(input()) for _ in range(3)]

if angle[0] + angle[1] + angle[2] == 180:
    if angle[0] == 60 and angle[1] == 60:
        print("Equilateral")
    elif angle[0] != angle[1] and angle[0] != angle[2] and angle[1] != angle[2]:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Error")