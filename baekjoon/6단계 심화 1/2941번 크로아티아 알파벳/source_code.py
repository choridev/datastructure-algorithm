c_alphabet = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
word = input()
i = 0

while i < len(word):
    if word[i:(i + 2)] in c_alphabet:
        count += 1
        i += 2
    elif word[i:(i + 3)] == 'dz=':
        count += 1
        i += 3
    else:
        count += 1
        i += 1

print(count)