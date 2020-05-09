dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
Q = []
visited = [[0] * M for _ in range(N)]

Q.append([0, 0])
visited[0][0] = 1
cnt = 1

while Q:
    NQ = []
    for r, c in Q:
        if r == N-1 and c == M-1:
            cnt=visited[r][c]
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0:
                continue
            if maze[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                NQ.append([nr, nc])
    Q = NQ

print(cnt)


