def bfs(i, j):
    size = 1
    queue = [[i, j]]
    visited[i][j] = 1
    while queue:
        new_queue = []
        for r, c in queue:
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                if visited[nr][nc]:
                    continue
                if space[nr][nc] == 1:
                    new_queue.append([nr, nc])
                    visited[nr][nc] = 1
                    size += 1
        queue = new_queue
    return size

n, m, k = map(int, input().split())
space = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    space[r-1][c-1] = 1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

ans = 0
for i in range(n):
    for j in range(m):
        if space[i][j]:
            ans = max(ans, bfs(i, j))
print(ans)