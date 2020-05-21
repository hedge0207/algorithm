import sys
sys.stdin = open("5248_input.txt", "r")


def f(x):
    for i in G[x]:
        if visited[i] == 0:
            visited[i] = 1
            f(i)

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    E = list(map(int, input().split()))
    G = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    
    for i in range(0, len(E), 2):
        s, e = E[i], E[i + 1]
        G[s].append(e)
        G[e].append(s)

    cnt = 0
    for i in range(1, N + 1):
        if visited[i] == 0:
            f(i)
            cnt += 1

    print("#{} {}".format(tc, cnt))