import sys

sys.stdin = open("5099_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    oven = []

    for i in range(len(Ci)):
        oven.append([Ci[i]//2, i+1])
        if len(oven) == N:
            while len(oven)==N:
                if oven[0][0]==0:
                    oven.pop(0)
                else:
                    a=oven[0][0]//2
                    b = oven[0][1]
                    oven.pop(0)
                    oven.append([a,b])

    while len(oven) != 1:
        if oven[0][0] == 0:
            oven.pop(0)
        else:
            a = oven[0][0] // 2
            b = oven[0][1]
            oven.pop(0)
            oven.append([a, b])

    print("#{} {}".format(tc,oven[0][1]))