import sys

sys.setrecursionlimit(1000000)


def f(s, e, c):
    global cnt, flag
    if s == G[e]:
        cnt += c+1
        flag = 1
    n = G[e]
    if visited[n] == 0:
        visited[n] = 1
        f(s, n, c)
        if not flag:
            visited[n]=0



for tc in range(int(input())):
    N = int(input())
    E = list(map(int, input().split()))
    G = [0] + E
    visited = [0] * (N + 1)
    tvisited = [0] * (N + 1)

    cnt = 0
    for i in range(1, len(G)):
        if i == G[i]:
            tvisited[i] = 1
            cnt += 1

    for i in range(1, len(G)):
        flag = 0
        if tvisited[i] == 0:
            f(i, i, 1)

    print(N - cnt)
