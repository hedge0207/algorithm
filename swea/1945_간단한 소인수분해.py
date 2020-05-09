import sys
sys.stdin = open("1945_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    pn = [2,3,5,7,11]
    pnn = []

    for i in pn:
        if N % i == 0:
            pnn += [i]

    pnnn=[]
    i = 0
    while i<len(pnn):
        if N % pnn[i] == 0:ㄴ
            N = N//pnn[i]
            pnnn += [pnn[i]]
        else:
            i += 1
    a = pnnn.count(2)
    b = pnnn.count(3)
    c = pnnn.count(5)
    d = pnnn.count(7)
    e = pnnn.count(11)

    print("#{} {} {} {} {} {}".format(tc,a,b,c,d,e))


#간단한 버전
# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     soinsu = [2, 3, 5, 7, 11]
#     result = []  # 2,3,5,7,11 소수
#
#     for i in soinsu:
#         cnt = 0
#         while n % i == 0:
#             n = n // i
#             cnt += 1
#         result.append(cnt)
#
#     print('#{} {}'.format(tc, ' '.join(map(str, result))))


