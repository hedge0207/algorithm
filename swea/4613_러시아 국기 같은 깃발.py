import sys

sys.stdin = open("4613_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    color = [input() for _ in range(N)]

    tcnt = []
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            a = color[:i + 1]
            b = color[i + 1:j + 1]
            c = color[j + 1:N]
            cnt=0

            for k in range(len(a)):
                for l in range(M):
                    if a[k][l] != "W":
                        cnt+=1
            for k in range(len(b)):
                for l in range(M):
                    if b[k][l] != "B":
                        cnt+=1
            for k in range(len(c)):
                for l in range(M):
                    if c[k][l] != "R":
                        cnt+=1
            tcnt+=[cnt]

    print("#{} {}".format(tc,min(tcnt)))







