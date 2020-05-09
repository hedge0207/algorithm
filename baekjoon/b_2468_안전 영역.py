#DFS풀이
import sys
sys.setrecursionlimit(1000000)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, rain):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= N or nr < 0 or nc >= N or nc < 0:
            continue
        if area[nr][nc] > rain and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            dfs(nr, nc, rain)


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
maxx = 0
for i in range(N):
    for j in range(N):
        if area[i][j] > maxx:
            maxx = area[i][j]

tcnt = []
for ra in range(1, maxx+1):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and area[i][j] > ra:
                visited[i][j]=1
                dfs(i, j, ra)
                cnt += 1
    tcnt += [cnt]

max_area=1
for i in tcnt:
    if i > max_area:
        max_area = i

print(max_area)



#BFS풀이
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# 
# def bfs(rain):
#     global Q
#     while Q:
#         NQ=[]
#         for r,c in Q:
#             for i in range(4):
#                 nr=r+dr[i]
#                 nc=c+dc[i]
#                 if nr >= N or nr < 0 or nc >= N or nc < 0:
#                     continue
#                 if area[nr][nc]>rain and visited[nr][nc]==0:
#                     visited[nr][nc]=1
#                     NQ.append([nr,nc])
#         Q=NQ
# 
# 
# 
# N = int(input())
# area = [list(map(int, input().split())) for _ in range(N)]
# maxx = 0
# for i in range(N):
#     for j in range(N):
#         if area[i][j] > maxx:
#             maxx = area[i][j]
# 
# tcnt = []
# for ra in range(1, maxx+1):
#     Q=[]
#     visited = [[0] * N for _ in range(N)]
#     cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j] == 0 and area[i][j] > ra:
#                 visited[i][j]=1
#                 Q.append([i,j])
#                 bfs(ra)
#                 cnt += 1
#     tcnt += [cnt]
# 
# max_area=1
# for i in tcnt:
#     if i > max_area:
#         max_area = i
# 
# print(max_area)