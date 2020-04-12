import sys
sys.setrecursionlimit(10**6)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:  #인덱스는 N-1, M-1이므로 N,M 보다 크거나 같으면 범위를 벗어난 값이다.
            continue
        if arr[nr][nc] == 1:
            arr[nr][nc] = 2
            dfs(nr, nc)


T = int(input())

for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    arr = [[0] * (M) for _ in range(N)]

    for i in range(K):
        r, c = map(int, input().split())
        arr[c][r] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                arr[i][j] = 2
                dfs(i, j)
                cnt += 1

    print(cnt)
