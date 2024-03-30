credit_sum = 0
score = 0

for i in range(20):
    string = input()
    if string[-1] == "P":
        continue
    elif string[-1] == "F":
        credit = float(string[-5:-2])
        credit_sum += credit
    else:
        grade = string[-2:]
        credit = float(string[-6:-3])
        credit_sum += credit
        match grade:
            case "A+":
                score += 4.5 * credit
            case "A0":
                score += 4.0 * credit
            case "B+":
                score += 3.5 * credit
            case "B0":
                score += 3.0 * credit
            case "C+":
                score += 2.5 * credit
            case "C0":
                score += 2.0 * credit
            case "D+":
                score += 1.5 * credit
            case "D0":
                score += 1.0 * credit
            case "F":
                score += 0 * credit

if credit_sum == 0:
    print(0.0)
else:
    print(score / credit_sum)