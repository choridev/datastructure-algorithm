word = input()

for char in word:
    if char.isupper():
        print(char.lower(), end='')
    else:
        print(char.upper(), end='')