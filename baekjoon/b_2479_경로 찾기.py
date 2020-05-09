# N, K =map(int,input().split())
# bn = []
# for i in range(N):
#     bn.append(input())
# st,ed = map(int,input().split())
# Q = [0]
# visited =[0]*(N+1)
# arr = [[0]*(N+1) for _ in range(N+1)]
# ans = []
#
# # 해밍 거리가 1인지 확인
# for i in range(N):
#     for j in range(N):
#         if i==j:
#             continue
#         cnt = 0
#         for k in range(K):
#             if bn[i][k]!=bn[j][k]:
#                 cnt+=1
#         if cnt==1:
#             arr[i+1][j+1]=1
#
# #BFS, BFS는 최단 경로를 보장하므로
# Q.append(st)
# visited[st]=1
# flag = 1
# while Q and flag:
#     t = Q.pop()
#     for i in range(len(arr[t])):
#         if arr[t][i]==1 and visited[i]==0:
#             visited[i]=visited[t]+1
#             Q.append(i)
#             ans.append([t,i])
#             if i == ed:     #도착지가 나왔다면 break
#                 flag = 0
#
#
#
# # st에서 ed까지의 경로를 구하는 코드
# a = ans[len(ans)-1][0]
# result = [ed,a]
# i = 0
# while a != st and i<len(ans):
#     if ans[i][1]==a:
#         a = ans[i][0]
#         i = 0
#         result.append(a)
#     else:
#         i+=1
# if flag:
#     print(-1)
# else:
#     for i in range(len(result)-1,-1,-1):
#         print(result[i],end=" ")


# 실패한 코드 1, BFS로 풀려 했으나 방문 순서대로 출력만 되고 최단거리는 출력을 못한 코드
# N, K =map(int,input().split())
# bn = []
# for i in range(N):
#     bn.append(input())
# st,ed = map(int,input().split())
# G = [[-1]*(N+1) for _ in range(N+1)]
# Q = [0]
# visited =[0]*(N+1)
# ans = []
#
# for i in range(N):
#     for j in range(N):
#         if i==j:
#             continue
#         cnt = 0
#         for k in range(K):
#             if bn[i][k]!=bn[j][k]:
#                 cnt+=1
#         G[i+1][j+1]=G[j+1][i+1]=cnt
# 
# Q.append(st)
# visited[st]=1
# ans.append(ed)
# print(G)
# while Q:
#     t = Q.pop()
#     for i in range(len(G[t])):
#         if G[t][i]==1 and visited[i]==0:
#             Q.append(i)
#             visited[i]=1
#             ans.append(i)
# 
# print(ans)


# 실패한 코드2, 모든 거리를 구한 후 그 중 최단 거리를 찾기 위해 DFS로 풀려 했으나 시간 초과로 풀지 못함
# def dfs(st,ed,route):
#     global ans
#     if st==ed:
#         ans.append(route[:])
#     else:
#         for i in range(len(arr[st])):
#             if arr[st][i] == 1 and visited[i] == 0:
#                 visited[i]=1
#                 route.append(i)
#                 dfs(i,ed,route)
#                 visited[i]=0
#                 route.pop()
#
# N, K =map(int,input().split())
# bn = []
# for i in range(N):
#     bn.append(input())
# st,ed = map(int,input().split())
# arr = [[0]*(N+1) for _ in range(N+1)]
# Q = [0]
# visited =[0]*(N+1)
#
# for i in range(N):
#     for j in range(N):
#         if i==j:
#             continue
#         cnt = 0
#         for k in range(K):
#             if bn[i][k]!=bn[j][k]:
#                 cnt+=1
#         if cnt==1:
#             arr[i+1][j+1]=1
# ans = []
#
# dfs(ed,st,[ed])
#
# result = ans[0]
# for i in ans:
#     if len(result)>len(i):
#         result=i
#
#
# for i in range(len(result)-1,-1,-1):
#     print(result[i],end=' ')



# 다른 사람의 코드
# from collections import deque
#
# def check(st,tmp):
#     cnt = 0
#     for i in range(K):
#         if code[st][i] != code[tmp][i]:
#             cnt += 1
#             if cnt == 2:
#                 return False
#     return True
#
# N, K = map(int,input().split())
# code = [0 for _ in range(N+1)]
# for i in range(1, N+1):
#     code[i] = input()
# A, B = map(int,input().split())
#
# visit = [False for _ in range(N+1)]
# q = deque()
# q.append((A,[A]))
# visit[A] = True
# ans = []
# while q:
#     st, path = q.popleft()
#     if check(st,B):
#         ans = path+[B]
#         break
#     for i in range(1,N+1):
#         if not visit[i] and check(st,i):
#             visit[i] = True
#             q.append((i,path+[i]))
#
# if ans:
#     print(' '.join(map(str,ans)))
# else:
#     print('-1')