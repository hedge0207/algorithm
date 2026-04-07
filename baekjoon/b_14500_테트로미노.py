N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_ = max(map(max, arr))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

v = [[0] * M for _ in range(N)]
def dfs(n, temp, lst):
    global ans

    if temp + (4 - n) * max_ <= ans:
        return

    if n == 4:
        ans = max(temp, ans)
        return

    for cx, cy in lst:
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and v[nx][ny] == 0:
                v[nx][ny] = 1
                dfs(n + 1, temp + arr[nx][ny], lst + [(nx, ny)])
                v[nx][ny] = 0


ans = 0
for i in range(N):
    for j in range(M):
        v[i][j] = 1
        dfs(1, arr[i][j], [(i, j)])

print(ans)