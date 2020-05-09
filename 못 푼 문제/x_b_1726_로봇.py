#아래 통과 못한 코드가 있음



# 통과 못한 누더기 코드
# dr = [0,1,0,-1]
# dc = [1,0,-1,0]
# direction = [1,3,2,4]
#
#
# R, C = map(int,input().split())
# factory = [list(map(int,input().split())) for _ in range(R)]
# sr,sc,sd = map(int,input().split())
# er,ec,ed = map(int,input().split())
# sr-=1;sc-=1;er-=1;ec-=1
# Q = []
# visited=[[[0]*C for _ in range(R)] for _ in range(4)]
#
#
# turn = 0
# go = 0
# more = 0
# Q.append([sr,sc,sd,turn,go,more,0])
# visited[0][sr][sc]=1;visited[1][sr][sc]=1;visited[2][sr][sc]=1;visited[3][sr][sc]=1
#
# result = 987654321
# ans= 0
# start = 1
# while Q:
#     NQ = []
#     for q in Q:
#         flag = 0
#         r,c,d,t,g,m,v=q
#         for i in range(4):
#             temp_d=d
#             temp_t=t
#             temp_g=g
#             temp_m=m
#             temp_v=v
#             nr = r+dr[i]
#             nc = c+dc[i]
#             if nr>=R or nc>=C or nr<0 or nc<0:
#                 continue
#             else:
#                 if factory[nr][nc]==0:
#                     if start:
#                         temp_v=i
#                     if visited[temp_v][nr][nc]==1:
#                         continue
#                     visited[temp_v][nr][nc]=1
#                     if d != direction[i]:
#                         flag = 1
#                         if abs(i-direction.index(temp_d))==2:
#                             temp_t += 2
#                         else:
#                             temp_t += 1
#                         temp_d=direction[i]
#                     if flag or start:
#                         temp_m += 1
#                         temp_g = 0
#
#                     temp_g += 1
#                     if temp_g == 4:
#                         temp_m += 1
#                         temp_g = 1
#                     NQ.append([nr,nc,temp_d,temp_t,temp_g,temp_m,temp_v])
#
#                 if nr == er and nc == ec:
#                     if ed != temp_d:
#                         if abs(direction.index(ed)-direction.index(temp_d))==2:
#                             temp_t += 2
#                         else:
#                             temp_t += 1
#                     print(temp_t,temp_m)
#                     result = min(result,temp_t+temp_m)
#     start = 0
#     Q = NQ
#
#
# if sr==er and sc==ec:
#     if sd==ed:
#         print(0)
#     else:
#        if abs(direction.index(sd)-direction.index(ed))==2:
#             print(2)
#        else:
#            print(1)
# else:
#     print(result)




#답
# from sys import stdin
# from collections import deque
# input = stdin.readline
#
# n, m = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]
# dist = [[[0]*4 for _ in range(m)] for _ in range(n)]
# sx, sy, sd = map(int, input().split())
# ex, ey, ed = map(int, input().split())
# dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
#
# def bfs():
#     q = deque()
#     q.append((sx-1, sy-1, sd-1))
#     while q:
#         x, y, d = q.popleft()
#         if x == ex-1 and y == ey-1 and d == ed-1:
#             print(dist[x][y][d])
#             return
#         for i in range(1, 4):
#             nx, ny = x+dx[d]*i, y+dy[d]*i
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 break
#             if a[nx][ny]:
#                 break
#             if not dist[nx][ny][d]:
#                 q.append((nx, ny, d))
#                 dist[nx][ny][d] = dist[x][y][d]+1
#         for i in range(4):
#             if i == d:
#                 continue
#             k = 2 if (i+d)%4 == 1 else 1
#             if not dist[x][y][i]:
#                 q.append((x, y, i))
#                 dist[x][y][i] = dist[x][y][d]+k
#
# bfs()
# 출처: https://rebas.kr/742 [PROJECT REBAS]