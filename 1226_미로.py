import sys

sys.stdin = open("1226_input.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r,c):
    global flag
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 16 <= nr or 0 > nr or 16 <= nc or 0 > nc:
            continue
        if maze[nr][nc] == 3:
            flag = 1
            return
        if maze[nr][nc] == 0:
            maze[nr][nc] = 1
            dfs(nr,nc)





for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                sr = r; sc = c
    flag = 0

    dfs(sr,sc)

    print("#{} {}".format(tc, flag))


