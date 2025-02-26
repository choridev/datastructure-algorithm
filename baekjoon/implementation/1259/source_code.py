import sys

def check_side(word):
    if len(word) == 0 or len(word) == 1:
        return True
    if word[0] == word[-1]:
        return check_side(word[1:-1])
    else:
        return False


while True:
    word = sys.stdin.readline().rstrip()
    if word == '0':
        break
    if check_side(word):
        print('yes')
    else:
        print('no')