word = input()

n =  len(word) // 2

for i in range(n):
    if word[i] != word[-i - 1]:
        print(0)
        exit()
print(1)