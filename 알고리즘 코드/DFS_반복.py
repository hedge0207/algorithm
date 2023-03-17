def dfs(v):
    s = []  #stack
    visited = [0]*(V+1)
    s.append(v)
    while s:
        u = s.pop()
        if visited[u]==0:
            print(u, end = " ")
            visited[u] = 1
            for i in range(1,V+1):
                if adj[u][i]==1 and visited[i]==0: #인접해 있고(간선이 있고) 방문한 적 없으면
                    s.append(i)


V, E = map(int,input().split())
edges = list(map(int,input().split()))

#인접행렬 생성
adj = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    s,e = edges[2*i], edges[2*i+1]
    #무향 그래프일 경우
    adj[s][e]=1
    # adj[e][s]=1
print(adj)
dfs(1)

'''
input
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''