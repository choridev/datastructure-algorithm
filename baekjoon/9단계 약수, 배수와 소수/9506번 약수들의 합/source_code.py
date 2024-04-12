while True:
    n = int(input())

    if n == -1:
        break
    
    divisor = []
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
            sum += i

    if n == sum:
        print(f"{n} = ", end="")
        for i in range(len(divisor)):
            print(f"{divisor[i]}", end="")
            if i != (len(divisor) - 1):
                print(" + ", end="")
            else:
                print()
    else:
        print(f"{n} is NOT perfect.")