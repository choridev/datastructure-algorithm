T = int(input()) # 테스트 케이스 개수

for i in range(T):
    R, S = input().split() # 반복 횟수와 반복할 문자열
    P = "" # 새로 만들 문자열
    for j in range(len(S)):
        for k in range(int(R)):
            P += S[j]
    print(P)