# import sys
# sys.stdin=open("5105_input.txt","r")
#
# dr=[-1,1,0,0]
# dc=[0,0,-1,1]
#
# def bfs(r,c,cc):
#     Q.append([r,c,cc])
#     visited[r][c]=1
#     while Q:
#         t = Q.pop(0)
#         a,b,d=t[0],t[1],t[2]
#         if not visited[a][b]:
#             visited[a][b]=1
#         for i in range(4):
#             nr=a+dr[i]
#             nc=b+dc[i]
#             if nr>=N or nr<0 or nc>=N or nc<0:
#                 continue
#             if maze[nr][nc]==3:
#                 return d-1
#             if maze[nr][nc]==0:
#                 if not visited[nr][nc]:
#                     maze[nr][nc]=1
#                     Q.append([nr,nc,d+1])
#     return 0
#
#
# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     maze=[list(map(int, input())) for _ in range(N)]
#     visited=[[0]*N for _ in range(N)]
#     Q=[]
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j]==2:
#                 print("#{} {}".format(tc,bfs(i,j,1)))


# DFS
import sys

sys.stdin = open("5105_input.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= N or nr < 0 or nc >= N or nc < 0:
            continue

        if maze[nr][nc] == 3:
            rlist.append(D[r][c])

        if maze[nr][nc] == 0:
            D[nr][nc] = D[r][c] + 1
            maze[nr][nc]=1
            dfs(nr, nc)
            maze[nr][nc]=0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    D = [[0] * N for _ in range(N)]

    rlist = []
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                dfs(i, j)

    if rlist:
        print("#{} {}".format(tc, min(rlist)))
    else:
        print("#{} {}".format(tc, 0))