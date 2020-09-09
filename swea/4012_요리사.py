import sys

sys.stdin = open("4012_input.txt", "r")


def f(k, cnt):
    global Min
    if cnt == N // 2:
        a = []
        b = []
        for i in range(N):
            if selected[i] == 1:
                a.append(i)
            else:
                b.append(i)

        sum_a = 0
        sum_b = 0
        for i in a:
            for j in a:
                sum_a += ing[i][j]
        for i in b:
            for j in b:
                sum_b += ing[i][j]

        if Min > abs(sum_a - sum_b):
            Min = abs(sum_a - sum_b)
        return

    if k == N:
        return

    selected[k] = 1
    f(k + 1, cnt + 1)
    selected[k] = 0
    f(k + 1, cnt)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ing = [list(map(int, input().split())) for _ in range(N)]
    selected = [0] * N
    Min = 0xffffff

    f(0, 0)
    print("#{} {}".format(tc, Min))
