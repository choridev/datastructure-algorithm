N, M = map(int, input().split())
basket_list = list(range(1, N + 1))

for i in range(M):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    temp_list = basket_list[start:(end + 1)]
    for j in range(start, end + 1):
        del(basket_list[j])
        basket_list.insert(j, temp_list.pop())

for i in range(N):
    print(basket_list[i], end=" ")