# deque를 안쓰면 시간초과 에러
# from collections import deque
#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# M, N = map(int, input().split())
# toma = [list(map(int, input().split())) for _ in range(N)]
# Q = deque([])
# visited = [[0] * M for _ in range(N)]
#
# for i in range(N):
#     for j in range(M):
#         if toma[i][j] == 1:
#             Q.append([i,j])
#             visited[i][j] = 1
#         if toma[i][j] == -1:
#             visited[i][j] = -1
#
#
# while Q:
#     t = Q.popleft()
#     a, b = t[0], t[1]
#     for i in range(4):
#         nr = a + dr[i]
#         nc = b + dc[i]
#         if nr >= N or nr < 0 or nc >= M or nc < 0:
#             continue
#         if visited[nr][nc] == 0:
#             Q.append([nr, nc])
#             visited[nr][nc] = visited[a][b] + 1
#
#
# Max=0
# flag=1
# for i in range(N):
#     for j in range(M):
#         if visited[i][j]==0:
#             flag=0
#             break
#         Max=max(Max,visited[i][j])
#
# if flag:
#     print(Max-1)
# else:
#     print(-1)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

M, N = map(int, input().split())
toma = [list(map(int, input().split())) for _ in range(N)]
Q = []
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if toma[i][j] == 1:
            Q.append([i, j])
            visited[i][j] = 1
        if toma[i][j] == -1:
            visited[i][j] = -1

while Q:
    NQ = []
    for r, c in Q:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr >= N or nr < 0 or nc >= M or nc < 0:
                continue
            if visited[nr][nc] == 0:
                Q.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1
    Q = NQ

Max=0
flag=1
for i in range(N):
    for j in range(M):
        if visited[i][j]==0:
            flag=0
            break
        Max=max(Max,visited[i][j])

if flag:
    print(Max-1)
else:
    print(-1)