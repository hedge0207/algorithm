import sys

sys.stdin = open("2814_input.txt", "r")


def dfs(n, cnt):
    global maxx

    if maxx < cnt:
        maxx = cnt

    for i in range(1, N + 1):
        if visited[i] == 0 and arr[n][i]:
            visited[i] = 1
            cnt += 1
            dfs(i, cnt)
            visited[i] = 0  # visited[i] = 0을 해주는 이유는 3번 case같은 경우가 있을 수 있기 때문이다.
            cnt -= 1

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * (N + 1)
    cnt = 1
    maxx = 0
    arr = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(M):
        u, v = map(int, input().split())
        arr[u][v] = 1
        arr[v][u] = 1

    for i in range(1, N + 1):
        visited[i] = 1
        dfs(i, cnt)
        visited[i] = 0

    print("#{} {}".format(tc, maxx))
