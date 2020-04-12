#deque 안쓰고 python으로 제출해 pass한 코드
#pop을 안쓰고 반복문을 돌린다.
M, N, H = map(int, input().split())
toma = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
Q = []

D = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if toma[i][j][k] == 1:
                Q.append([i, j, k])
                day = 1


while Q:
    NQ = []
    for h, r, c in Q:
        for dh, dr, dc in D:
            nh = h + dh
            nr = r + dr
            nc = c + dc
            if nh >= H or nh < 0 or nr >= N or nr < 0 or nc >= M or nc < 0:
                continue
            if toma[nh][nr][nc] == 0:
                toma[nh][nr][nc] = day
                NQ.append([nh, nr, nc])

    Q = NQ
    day += 1

day-=1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if toma[i][j][k] == 0:
                day = -1

print(day)







#deque를 안썼으나 python에서 시간초과가 발생한 코드
# M, N, H = map(int, input().split())
# toma = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# visited = [[[0] * M for _ in range(N)] for _ in range(H)]
# Q = []
#
# D = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
#
# day = 0
# for i in range(H):
#     for j in range(N):
#         for k in range(M):
#             if toma[i][j][k] == 1:
#                 Q.append([i, j, k])
#                 visited[i][j][k] = 1
#                 day = 1
#             if toma[i][j][k] == -1:
#                 visited[i][j][k] = -1
#
# while True:
#     NQ = []
#     for h, r, c in Q:
#         for dh, dr, dc in D:
#             nh = h + dh
#             nr = r + dr
#             nc = c + dc
#             if nh >= H or nh < 0 or nr >= N or nr < 0 or nc >= M or nc < 0:
#                 continue
#             if visited[nh][nr][nc] == 0:
#                 visited[nh][nr][nc] = day
#                 NQ.append([nh, nr, nc])
#     if len(NQ) == 0:
#         break
#     Q = NQ
#     day += 1
#
# day-=1
# for i in range(H):
#     for j in range(N):
#         for k in range(M):
#             if visited[i][j][k] == 0:
#                 day = -1
#                 break
#
# print(day)










# deque와 pypy를 사용해서 통과
# from collections import deque
#
# dr = [-1,1,0,0]
# dc = [0,0,-1,1]
# dh = [0,-1,1]
#
# def bfs():
#     Max=0
#     while Q:
#         t = Q.popleft()
#         c,a,b=t[0],t[1],t[2]
#         Max = max(Max, visited[c][a][b])
#         for h in range(3):
#             nh = c+dh[h]
#             if nh>=H or nh<0:
#                 continue
#             if h==0:
#                 for i in range(4):
#                     nr = a+dr[i]
#                     nc = b+dc[i]
#                     if nr>=N or nr<0 or nc>=M or nc<0:
#                         continue
#                     if toma[nh][nr][nc]==0 and visited[nh][nr][nc]==0:
#                         visited[nh][nr][nc]=visited[nh][a][b]+1
#                         Q.append([nh,nr,nc])
#
#
#             else:
#                 if toma[nh][a][b]==0 and visited[nh][a][b]==0:
#                     Q.append([nh,a,b])
#                     visited[nh][a][b]=visited[c][a][b]+1
#
#     return Max
#
#
#
#
# M,N,H=map(int, input().split())
# toma = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# visited=[[[0]*M for _ in range(N)] for _ in range(H)]
# Q=deque([])
#
#
# a = 0
# flag=0
# ble = 0
# for h in range(H):
#     for i in range(N):
#         for j in range(M):
#             if toma[h][i][j]==-1:
#                 visited[h][i][j]=-1
#             if toma[h][i][j]==1:
#                 Q.append([h,i,j])
#                 visited[h][i][j] = 1
#                 ble=1
#             if toma[h][i][j]==0:
#                 flag=1
#
# if ble == 0:
#     print(-1)
# else:
#     if flag:
#         a = bfs()-1
#         fg=1
#         for h in range(H):
#             for i in range(N):
#                 for j in range(M):
#                     if visited[h][i][j] == 0:
#                         fg=0
#                         break
#         if fg:
#             print(a)
#         else:
#             print(-1)
#
#     else:
#         print(0)
