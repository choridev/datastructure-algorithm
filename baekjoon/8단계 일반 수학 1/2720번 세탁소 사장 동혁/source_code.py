T = int(input())

for i in range(T):
    change = int(input())
    quarter = change // 25
    change %= 25
    dime = change // 10
    change %= 10
    nickel = change // 5
    change %= 5
    penny = change
    print(quarter, dime, nickel, penny)