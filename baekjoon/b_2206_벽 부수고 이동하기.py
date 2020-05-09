# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# N, M = map(int, input().split())
# mapp = [list(map(int, input())) for _ in range(N)]
# Q = []
# visited = [[[0] * M for _ in range(N)] for _ in range(2)]
# Q.append([1, 0, 0])
# visited[1][0][0] = 1
# visited[0][0][0] = 1
# cnt = 987654321
# flag = 0
# while Q:
#     NQ = []
#     for b, r, c in Q:
#         if r==N-1 and c==M-1:
#             flag=1
#             if cnt>visited[b][r][c]:
#                 cnt=visited[b][r][c]
#
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if nr >= N or nc >= M or nr < 0 or nc < 0:
#                 continue
#             if b == 1:
#                 if mapp[nr][nc] == 0 and visited[b][nr][nc] == 0:
#                     visited[b][nr][nc] = visited[b][r][c]+1
#                     NQ.append([b, nr, nc])
#                 elif mapp[nr][nc] == 1 and visited[0][nr][nc] == 0:
#                     visited[0][nr][nc] = visited[b][r][c]+1
#                     NQ.append([0, nr, nc])
#             else:
#                 if mapp[nr][nc] == 0 and visited[b][nr][nc] == 0:
#                     visited[b][nr][nc] = visited[b][r][c]+1
#                     NQ.append([b, nr, nc])
#     Q=NQ
#     for k in range(2):
#         for i in range(N):
#             for j in range(M):
#                 if k==0:
#                     print(visited[k][i][j], end=" ")
#                 else:
#                     print(visited[k][i][j], end=" ")
#
#             print()
#         print()
#     print()

# if flag:
#     print(cnt)
# else:
#     print(-1)



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
mapp = [list(map(int, input())) for _ in range(N)]
Q = []

# 벽을 부순 경우와 부수지 않은 경우를 따로 표시하기 위한 리스트
visited = [[[0] * M for _ in range(N)] for _ in range(2)]
Q.append([1, 0, 0])
visited[1][0][0] = 1
visited[0][0][0] = 1
cnt = 987654321
flag = 0

while Q:
    NQ = []
    for b, r, c in Q:
        if r==N-1 and c==M-1:  #목표 지점에 도달 했으면
            flag=1
            if cnt>visited[b][r][c]:
                cnt=visited[b][r][c]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nc >= M or nr < 0 or nc < 0:
                continue
            if b == 1:  #벽을 부수지 않았으면
                if mapp[nr][nc] == 0 and visited[b][nr][nc] == 0: #1칸 이동
                    visited[b][nr][nc] = visited[b][r][c]+1
                    NQ.append([b, nr, nc])
                elif mapp[nr][nc] == 1 and visited[0][nr][nc] == 0: #벽을 만나면 벽을 부순다
                    visited[0][nr][nc] = visited[b][r][c]+1
                    NQ.append([0, nr, nc])
            else:
                if mapp[nr][nc] == 0 and visited[b][nr][nc] == 0:
                    visited[b][nr][nc] = visited[b][r][c]+1
                    NQ.append([b, nr, nc])
    Q=NQ

if flag:
    print(cnt)
else:
    print(-1)







# 시간초과
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
#
# def bfs(row, column, br, li):
#     global Q, Min, flag
#     li.append([row, column])
#     Q.append([row, column, br, li])
#     a = 0
#     while Q:
#         print(len(Q))
#         NQ = []
#         for r, c, b, l in Q:
#             nl=[]
#             if r == N - 1 and c == M - 1:
#                 flag=True
#                 if Min>a:
#                     Min=a
#                 break
#             for i in range(4):
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 if nr >= N or nc >= M or nr < 0 or nc < 0 or [nr,nc] in l:
#                     continue
#                 if arr[nr][nc] == 0:
#                     nl.append([nr,nc])
#                     NQ.append([nr,nc,b,l+nl])
#                 else:
#                     if b==1:
#                         NQ.append([nr,nc,0,l])
#         Q = NQ
#         a += 1
#     return Min
#
#
# N, M = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
# Q = []
# Min = 987654321
# flag=False
#
# a = bfs(0, 0, 1,[])
# if flag:
#     print(a+1)
# else:
#     print(-1)
