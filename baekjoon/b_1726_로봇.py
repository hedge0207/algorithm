from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

map_dir = {0: 0, 1: 2, 2: 1, 3: 3}

n, m = map(int, input().split())
factory = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0]*4 for _ in range(m)] for _ in range(n)]
st_r, st_c, st_di = map(int, input().split())
queue = deque()
st_di = map_dir[st_di-1]
queue.append((st_r-1, st_c-1, st_di, 0))
visited[st_r-1][st_c-1][st_di] = 1
de_r, de_c, de_di = map(int, input().split())
de_r -= 1
de_c -= 1
de_di = map_dir[de_di-1]

while queue:
    r, c, d, cnt = queue.popleft()
    if r == de_r and c == de_c and de_di == d:
        print(cnt)
        break
    for i in range(4):
        if i != d:
            for j in range(-1, 2, 2):
                new_d = (d + j) % 4
                if visited[r][c][new_d]:
                    continue
                visited[r][c][new_d] = 1
                queue.append((r, c, new_d, cnt+1))
            continue
        for j in range(1, 4):
            nr, nc = r + dr[i] * j, c + dc[i] * j
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if visited[nr][nc][i]:
                continue

            if factory[nr][nc]:
                break

            visited[nr][nc][i] = 1
            queue.append((nr, nc, i, cnt+1))
    cnt += 1