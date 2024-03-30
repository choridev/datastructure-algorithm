N = int(input())
count = 0

for i in range(N):
    word = input()
    token = []
    # 단어의 알파벳 개수만큼 반복
    for j in range(len(word)):
        target = word[j]
        # 단어의 첫 알파벳은 바로 토큰에 추가
        if j == 0:
            token.append(target)
        else:
            # 이전 순서의 알파벳과 지금 순서의 알파벳 비교
            last_token = token.pop()
            if target == last_token:
                token.append(last_token)
            elif target != last_token:
                token.append(last_token)
                if target in token:
                    break
                else:
                    token.append(target)
        if j == len(word) - 1:
            count += 1
print(count)
