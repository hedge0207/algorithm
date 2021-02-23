import sys

sys.setrecursionlimit(100000)

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(r, c):
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= h or nr < 0 or nc >= w or nc < 0:
            continue
        if area[nr][nc] == 1:
            area[nr][nc] = 9
            dfs(nr, nc)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    area = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if area[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)
