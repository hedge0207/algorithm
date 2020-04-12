dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    global Max
    Q.append([r, c])
    visited[r][c]=1

    while Q:
        t = Q.pop(0)
        a, b = t[0], t[1]
        Max = max(Max, visited[a][b])

        for i in range(4):
            nr = a + dr[i]
            nc = b + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0:
                continue
            if map[nr][nc] == "L" and visited[nr][nc] == 0:
                Q.append([nr, nc])
                visited[nr][nc] = visited[a][b] + 1
    return Max


N, M = map(int, input().split())
map = [list(input()) for _ in range(N)]
Q = []

Max = 0
for i in range(N):
    for j in range(M):
        if map[i][j] == "L":
            visited = [[0] * M for _ in range(N)]
            bfs(i, j)

print(Max-1)
