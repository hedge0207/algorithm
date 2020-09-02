import sys
sys.stdin = open("1226_input.txt", "r")

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
#
# def dfs(r, c):
#     global flag
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 16 <= nr or 0 > nr or 16 <= nc or 0 > nc:
#             continue
#         if maze[nr][nc] == 3:
#             flag = 1
#             return
#         if maze[nr][nc] == 0:
#             maze[nr][nc] = 1
#             dfs(nr, nc)
#
#
# for _ in range(1, 11):
#     tc = int(input())
#     maze = [list(map(int, input())) for _ in range(16)]
#     for r in range(16):
#         for c in range(16):
#             if maze[r][c] == 2:
#                 sr = r;
#                 sc = c
#     flag = 0
#
#     dfs(sr, sc)
#
#     print("#{} {}".format(tc, flag))

# 200902 재풀이
#dfs-재귀
# dr = [-1,1,0,0]
# dc = [0,0,-1,1]
# def dfs(r,c):
#     global flag
#     if flag:
#         return
#     for i in range(4):
#         nr = r+dr[i]
#         nc = c+dc[i]
#         if 16<=nr or 0>nr or 16<=nc or 0>nc:
#             continue
#         if maze[nr][nc]==3:
#             flag = 1
#         if maze[nr][nc]==0:
#             maze[nr][nc]=1
#             dfs(nr,nc)
#
#
# for _ in range(10):
#     tc = int(input())
#     maze = [list(map(int, input())) for _ in range(16)]
#     for r in range(16):
#         for c in range(16):
#             if maze[r][c] == 2:
#                 sr = r
#                 sc = c
#     flag = 0
#     dfs(sr,sc)
#     print("#{} {}".format(tc,flag))


#dfs-반복
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def dfs(r,c):
    global flag
    stack = []
    stack.append([r,c])
    while stack:
        cr,cc = stack.pop()
        for i in range(4):
            nr = cr+dr[i]
            nc = cc+dc[i]
            if 16<=nr or 0>nr or 16<=nc or 0>nc:
                continue
            if maze[nr][nc]==3:
                flag = 1
                return
            if maze[nr][nc]==0:
                maze[nr][nc]=1
                stack.append([nr,nc])

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                sr = r
                sc = c
    flag = 0
    dfs(sr,sc)
    print("#{} {}".format(tc,flag))

#bfs
# dr = [-1,1,0,0]
# dc = [0,0,-1,1]
# def bfs(r,c):
#     global flag
#     Q = []
#     Q.append([r,c])
#
#     while Q:
#         NQ = []
#         for r,c in Q:
#             for i in range(4):
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 if 16 <= nr or 0 > nr or 16 <= nc or 0 > nc:
#                     continue
#                 if maze[nr][nc]==3:
#                     flag=1
#                     return
#                 if maze[nr][nc]==0:
#                     NQ.append([nr,nc])
#                     maze[nr][nc]=1
#         Q = NQ
#
#
# for _ in range(10):
#     tc = int(input())
#     maze = [list(map(int, input())) for _ in range(16)]
#     for r in range(16):
#         for c in range(16):
#             if maze[r][c] == 2:
#                 sr = r
#                 sc = c
#     flag = 0
#     bfs(sr,sc)
#     print("#{} {}".format(tc,flag))