import sys
sys.stdin = open('5188_input.txt', 'r')


def dfs(r, c, d):
    global Min
    if r == N - 1 and c == N - 1:
        Min = min(Min, d)
        return
    elif d > Min:
        return
    else:
        if r + 1 < N:
            dfs(r + 1, c,  d + mapp[r + 1][c])
        if c + 1 < N:
            dfs(r, c + 1, d+ mapp[r][c + 1])


for tc in range(1, int(input()) + 1):
    N = int(input())
    mapp = [list(map(int, input().split())) for _ in range(N)]
    Min = 987654321
    dfs(0, 0, mapp[0][0])
    print(Min)
