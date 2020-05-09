N = int(input())
st,ed = map(int,input().split())
M = int(input())
G = [[] for _ in range(N+1)]
visited = [0]*(N+1)
Q = []


for i in range(M):
    p,c = map(int,input().split())
    G[p].append(c)
    G[c].append(p)

Q.append(st)

while Q:
    t = Q.pop(0)
    for i in G[t]:
        if not visited[i]:
            visited[i]=visited[t]+1
            Q.append(i)
if visited[ed]:
    print(visited[ed])
else:
    print(-1)



#DFS
# def dfs(st,cnt):
#     global ans
#     if st == ed:
#         ans=cnt
#         return
#     else:
#         for i in G[st]:
#             if visited[i] == 0:
#                 visited[i]=1
#                 dfs(i,cnt+1)
#                 visited[i]=0
#
#
# N = int(input())
# st,ed = map(int,input().split())
# M = int(input())
# G = [[] for _ in range(N+1)]
# ans = 0
# visited = [0]*(N+1)
#
# for i in range(M):
#     p,c = map(int,input().split())
#     G[p].append(c)
#     G[c].append(p)
#
# dfs(st,0)
# if ans:
#     print(ans)
# else:
#     print(-1)
